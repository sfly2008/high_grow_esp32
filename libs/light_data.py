from utime import sleep_ms
from machine import Pin, I2C
from libs.data_cfg import CfgData


class LightData:

    def __init__(self):
        self.Cfg = CfgData()
        self._I2C = I2C(scl=Pin(self.Cfg.BH_SCL), sda=Pin(self.Cfg.BH_SDA))
        self.READ_MODE = self.Cfg.BH_LOW_ONCE
        self.ON_MODE = self.Cfg.BH_ON
        self.OFF_MODE = self.Cfg.BH_OFF
        self.RST_MODE = self.Cfg.BH_RESET
        self.ADDR = self.Cfg.BH_ADDR
        self.PWR = Pin(self.Cfg.PWR_PIN, Pin.Out, value=1)
        self.setup()

    def set_state(self, state):
        self._I2C.writeto(self.ADDR, bytes([state]))

    def setup(self):
        self.set_state(self.OFF_MODE)
        self.set_state(self.ON_MODE)
        self.set_state(self.RST_MODE)

    def light_data(self):
        self.set_state(self.READ_MODE)
        sleep_ms(24)
        data = self._I2C.readfrom(self.ADDR, 2)
        self.PWR.value(0)
        return (data[0] << 8 | data[1])/1.2
