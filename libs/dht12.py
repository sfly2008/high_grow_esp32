from machine import Pin
from utime import sleep_ms
from dht import DHT11
from libs.data_cfg import CfgData


class DhtData:

    def __init__(self):
        self.Cfg = CfgData()
        self.PWR = Pin(self.Cfg.PWR_PIN, Pin.OUT, value=1)
        self.PIN = Pin(self.Cfg.DHT_PIN)
        self.WAIT = 2000
        self.SENSOR = DHT11(self.PIN)

    def temp_data(self):
        self.SENSOR.measure()
        sleep_ms(self.WAIT)
        return self.SENSOR.temperature()

    def hmdt_data(self):
        self.SENSOR.measure()
        sleep_ms(self.WAIT)
        return self.SENSOR.humidity()
