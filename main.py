from libs.light_data import LightData
from libs.dht12 import DhtData
from libs.salt_data import SaltData
from libs.soil_data import SoilData
from libs.vbat_data import VBatData
from machine import Pin

pwr_pin = Pin(4, Pin.OUT)
pwr_pin.value(1)


class SensorsData:

    def __init__(self):
        self.LIGHT = LightData()
        self.DHT = DhtData()
        self.SALT = SaltData()
        self.SOIL = SoilData()
        self.VBAT = VBatData()

    def all_data(self):
        data = {
            "Light": self.light,
            "Temp": self.temp,
            "Hmdt": self.hmdt,
            "Soil": self.soil,
            "Salt": self.salt,
            "Bat": self.vbat
        }
        return data

    def temp(self):
        return self.DHT.temp_data()

    def hmdt(self):
        return self.DHT.hmdt_data()

    def light(self):
        return self.LIGHT.light_data()

    def soil(self, samples=10):
        self.SOIL.soil_data(samples=samples)

    def salt(self):
        return self.SALT.salt_data()

    def vbat(self):
        return self.VBAT.read_bat()


sensors = SensorsData()
