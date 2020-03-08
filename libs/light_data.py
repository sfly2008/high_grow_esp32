from utime import sleep_ms
from machine import Pin, I2C

_modes = {
    "LOW_ONCE": 0x23,
    "LOW_CONT": 0x13,
    "HIGH1_ONCE": 0x20,
    "HIGH2_ONCE": 0x21,
    "HIGH1_CONT": 0x10,
    "HIGH2_CONT": 0x11
}


class LightData:

    def __init__(self, address=0x23, scl_pin=26, sda_pin=25):
        self.SCL_PIN = Pin(scl_pin)
        self.SDA_PIN = Pin(sda_pin)
        self.LIGHT_I2C = I2C(scl=self.SCL_PIN, sda=self.SDA_PIN)
        self.ADDR = address
        self.setup()

    def set_state(self, state):
        self.LIGHT_I2C.writeto(self.ADDR, bytes([state]))

    def setup(self):
        self.set_state(0x00)
        self.set_state(0x01)
        self.set_state(0x07)

    def light_data(self, read_mode=0x23):
        self.set_state(read_mode)
        sleep_ms(24)
        data = self.LIGHT_I2C.readfrom(self.ADDR, 2)
        return (data[0] << 8 | data[1])/1.2
