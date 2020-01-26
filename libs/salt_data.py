from machine import Pin, ADC
import utime
from libs.data_cfg import CfgData


class SaltData:
    def __init__(self):
        self.Cfg = CfgData()
        self._PIN = Pin(self.Cfg.SALT_PIN)
        self._PWR_PIN = Pin(4, Pin.OUT)
        self.SAMPLES = self.Cfg.SALT_DATA_SAMPLES
        self.HMD = 0
        self._ADC = ADC(self._PIN)
        self.DATA_ARR = []

    def salt_data(self):
        self._PWR_PIN.value(1)
        for i in range(self.SAMPLES):
            self.DATA_ARR.append(self._ADC.read())
            utime.sleep_ms(20)
        for item in self.DATA_ARR:
            if item == 0 or item == (self.SAMPLES - 1):
                pass
            else:
                self.HMD += item
        self._PWR_PIN.value(0)
        return self.HMD/(self.SAMPLES - 2)
