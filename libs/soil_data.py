from machine import Pin, ADC
from utime import sleep_ms


class SoilData:

    def __init__(self, soil_pin=32):
        self.PIN = soil_pin
        self.SOIL_ADC = ADC(Pin(self.PIN))
        self.SOIL_ADC.atten(ADC.ATTN_11DB)
        self.SOIL_ADC.width(ADC.WIDTH_12BIT)

    def soil_data(self, samples=13):
        data_cum = 0
        for i in range(samples):
            data_cum += self.SOIL_ADC.read()
            sleep_ms(2000)
        return data_cum/samples
