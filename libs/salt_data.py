from machine import Pin, ADC
from utime import sleep_ms


class SaltData:
    def __init__(self, salt_pin=34, samples=120):
        self.SALT_PIN = Pin(salt_pin)
        self.SAMPLES = samples
        self.SALT_ADC = ADC(self.SALT_PIN)

    def salt_data(self):
        data_cumulative = []
        salt = 0
        for i in range(self.SAMPLES):
            data_cumulative.append(self.SALT_ADC.read())
            sleep_ms(20)
        for item in data_cumulative:
            if item == 0 or item == (self.SAMPLES - 1):
                pass
            else:
                salt += item
        return salt/(self.SAMPLES - 2)
