from machine import Pin, ADC
from utime import sleep_ms
from libs.data_cfg import CfgData


class SoilData:

    def __init__(self):
        self.Cfg = CfgData()
        self.PIN = Pin(self.Cfg.SOIL_PIN)
        self._ADC = ADC(self.PIN)
        self.SAMPLES = self.Cfg.SOIL_SAMPLES
        self.PWR = Pin(self.Cfg.PWR_PIN, Pin.OUT, value=0)

    def soil_data(self):
        data_cum = 0
        self.PWR.value(1)
        for _ in range(self.SAMPLES):
            data_cum += self._ADC.read()
            sleep_ms(2000)
        self.PWR.value(0)
        return data_cum/self.SAMPLES
