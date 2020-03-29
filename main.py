from libs.light_data import LightData
from libs.dht12 import DhtData
from libs.salt_data import SaltData
from libs.soil_data import SoilData
from libs.vbat_data import VBatData
from machine import Pin
from rest_srvr import RstServer
from time import sleep

pwr_pin = Pin(4, Pin.OUT)
pwr_pin.value(1)
sleep(2)
serv = RstServer()
try:
    serv.start_server()
except OSError:
    print('Sensors not ready, retrying ...')
    pwr_pin.value(1)
    sleep(3)
finally:
    serv.start_server()
