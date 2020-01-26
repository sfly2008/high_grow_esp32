from libs.data_cfg import CfgData
from libs.light_data import LightData
from libs.dht12 import DhtData
from libs.salt_data import SaltData
from libs.soil_data import SoilData
from machine import Pin


class AggrData:

    def __init__(self):
        self.Cfg = CfgData()
        self.PWR = Pin(self.Cfg.PWR_PIN, Pin.OUT, value=1)
        self.LIGHT = LightData()
        self.DHT = DhtData()
        self.SALT = SaltData()
        self.SOIL = SoilData()

    def all_data(self):
        if self.PWR.value() != 1:
            self.PWR.value(1)
        else:
            pass
        return ("Light: {} lx\nTemp: {} C\nHumidity: {}\nSoil: {}\nSalt: {}"
                .format(self.light(), self.temp(), self.hmdt(), self.soil(),
                        self.salt()))

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


aggr = AggrData()
