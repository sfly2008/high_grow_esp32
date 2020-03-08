from libs.light_data import LightData
from libs.dht12 import DhtData
from libs.salt_data import SaltData
from libs.soil_data import SoilData
from machine import Pin


class SensorsData:

    def __init__(self, power_pin=4):
        self.PWR = Pin(power_pin, Pin.OUT)
        self.LIGHT = LightData()
        self.DHT = DhtData()
        self.SALT = SaltData()
        self.SOIL = SoilData()

    def all_data(self):
        self.turn_power(on=True)
        return ("Light: {} lx\nTemp: {} C\nHumidity: {}\nSoil: {}\nSalt: {}"
                .format(self.light(), self.temp(), self.hmdt(), self.soil(),
                        self.salt()))

    def turn_power(self, on=True):
        if on:
            self.PWR.value(1)
        elif not on:
            self.PWR.value(0)
        else:
            raise ValueError("Only 'True' or 'False' values allowed as "
                             "input parameter")

    def temp(self):
        self.turn_power()
        return self.DHT.temp_data()

    def hmdt(self):
        self.turn_power()
        return self.DHT.hmdt_data()

    def light(self):
        self.turn_power()
        return self.LIGHT.light_data()

    def soil(self):
        self.turn_power()
        self.SOIL.soil_data()

    def salt(self):
        self.turn_power()
        return self.SALT.salt_data()


sensors = SensorsData()
