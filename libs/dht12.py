from machine import Pin
from utime import sleep_ms
from dht import DHT11


class DhtData:

    def __init__(self, dht_pin=16, wait_time_ms=2000):
        self.PIN = dht_pin
        self.WAIT = wait_time_ms
        self.SENSOR = DHT11(Pin(self.PIN))

    def temp_data(self):
        self.SENSOR.measure()
        sleep_ms(self.WAIT)
        return self.SENSOR.temperature()

    def hmdt_data(self):
        self.SENSOR.measure()
        sleep_ms(self.WAIT)
        return self.SENSOR.humidity()

    def read_all(self):
        return "Temp: {}; Hmdt: {}".format(self.temp_data(), self.hmdt_data())
