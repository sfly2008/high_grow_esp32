from machine import Pin, ADC


class VBatData:

    def __init__(self, vbat_pin=33):
        self.VBAT_PIN = Pin(vbat_pin)
        self.VBAT_ADC = ADC(self.VBAT_PIN)
        self.VBAT_ADC.atten(ADC.ATTN_11DB)
        self.VBAT_ADC.width(ADC.WIDTH_12BIT)
        self.VBAT_REF = 1100

    def read_bat(self):
        vbat_raw = self.VBAT_ADC.read()/4095 * 2 * 3.3 * self.VBAT_REF
        return vbat_raw
