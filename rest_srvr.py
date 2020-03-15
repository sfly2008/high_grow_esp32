import usocket
import sys
from machine import Pin
from libs.light_data import LightData
from libs.dht12 import DhtData
from libs.salt_data import SaltData
from libs.Soil_data import SoilData
from libs.vbat_data import VBatData


class SensorsData:

    def __init__(self, power_pin=4):
        self.PWR = Pin(power_pin, Pin.OUT)
        self.LIGHT = LightData()
        self.DHT = DhtData()
        self.SALT = SaltData()
        self.SOIL = SoilData()
        self.VBAT = VBatData()

    def all_data(self):
        data_dict = {
            "Light": self.light,
            "Temp": self.temp,
            "Hmdt": self.hmdt,
            "Soil": self.soil,
            "Salt": self.salt,
            "Bat": self.vbat
        }
        return data_dict

    def temp(self):
        return self.DHT.temp_data()

    def hmdt(self):
        return self.DHT.hmdt_data()

    def light(self):
        return self.LIGHT.light_data()

    def soil(self):
        self.SOIL.soil_data()

    def salt(self):
        return self.SALT.salt_data()

    def vbat(self):
        return self.VBAT.read_bat()


class RstServer:

    def __init__(self, address='', port=8989):
        self.ADDR = address
        self.PORT = port
        self.SERVER = usocket.socket()
        self.SDATA = SensorsData()
        self.ENDPOINTS = {
            "light": self.SDATA.light,
            "temp": self.SDATA.temp,
            "hmdt": self.SDATA.hmdt,
            "soil": self.SDATA.soil,
            "salt": self.SDATA.salt,
            "vbat": self.SDATA.vbat
        }

    def start_server(self):
        self.SERVER.bind((self.ADDR, self.PORT))
        self.SERVER.listen(2)
        print("Starting local rest server on port {}".format(self.PORT))
        while True:
            (socket, socket_addr) = self.SERVER.accept()
            try:
                self.handle(socket)
            except KeyboardInterrupt:
                print("Terminating server per user request...")
                socket.close()
            finally:
                print("Final block")
                socket.close()

    def get_header(self):
        return b"""HTTP/1.0 200 OK
        Content-Type: text/html; charset=utf-8
        Access-Control-Allow-Origin: *
        \r\n
        
        """

    def snd_resp(self, socket, data):
        socket.send(self.get_header())
        socket.send(b"""{}""".format(data))

    def snd_err(self, socket, err_code, err_msg):
        socket.write(b"""HTTP/1.1 401 NOK""" + err_code + b""": """ + err_msg)

    def handle(self, socket):
        method, url, vers = socket.readline().split(b""" """)
        url = str(url.decode('utf-8'))
        method = str(method.decode('utf-8'))
        vers = str(vers.decode('utf-8'))
        print("Url: {}\nMethod: {}\nVersion: {}".format(url, method, vers))
        path, query = url.split("/", 2)
        query = query.replace('?', '')
        print("Path: {}\nQuery: {}".format(path, query))
        while True:
            header = str(socket.readline().decode('utf-8'))
            if header == "":
                return
            if header == "\r\n":
                break
        if method == 'GET':
            if path == "":
                if query in self.ENDPOINTS.keys():
                    data = self.ENDPOINTS[query]()
                    resp = {query: data}
                    self.snd_resp(socket, resp)
                else:
                    print("Invalid endpoint specified: {}".format(query))
                    self.snd_err(socket, b"""401""", b"""Invalid endpoint 
                    specified: {}""".format(query))
            else:
                print("Invalid path specified: {}".format(path))
                self.snd_err(socket, b"""404""", b"""Invalid path:{}""".format(
                    path))
        else:
            print("Method '{}' is not implemented".format(method))
            self.snd_err(socket, b"""500""", b"""Method '{}' is not 
            implemented""".format(method))
