
class CfgData:
    def __init__(self):
        self.PWR_PIN = 4
        self.SALT_PIN = 34
        self.DHT_PIN = 16
        self.SOIL_PIN = 32
        self.BH_SDA = 25
        self.BH_SCL = 26
        self.BH_LOW_CONT = 0x13
        self.BH_HIGH1_CONT = 0x10
        self.BH_HIGH2_CONT = 0x11
        self.BH_HIGH1_ONCE = 0x20
        self.BH_HIGH2_ONCE = 0x21
        self.BH_ADDR = 0x23
        self.BH_LOW_ONCE = 0x23
        self.BH_OFF = 0x00
        self.BH_ON = 0x01
        self.BH_RESET = 0x07
        self.BOARD_SDA = 22
        self.BOARD_SCL = 21
        self.SALT_DATA_SAMPLES = 120
        self.SOIL_SAMPLES = 13
