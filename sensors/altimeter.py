import smbus
import time

class Altimeter:
    """
    A class defined to interface with the MS5803 altimeter for Real-Time-Rocket.
    """
    def __init__(self):
        """
        Create an altimeter object.
        """
        self._c = [
            0,
            0,
            0,
            0,
            0,
            0
            ]
        self._address = 0x77 #Hardware address on the altimeter
        self._prom_commands = [
            0xA0,
            0xA2,
            0xA4,
            0xA6,
            0xA8,
            0xAA,
            0xAC
            ]
        self._bus = smbus.SMBus(2)
        self._reset_command = 0x1E
        self._convert_d1_4096 = 0x48
        self._convert_d2_4096 = 0x58
    def initialize(self):
        """
        Initialize the altimeter. Called once at the start of using this altimeter.
        """
        print("Reading PROM")
        self.update_prom()
    def update_prom(self):
        """
        Update the information in self._c to reflect the values in PROM.
        """
        for i in range(len(self._prom_commands)):
            self._c[i] = self.read_prom(self._prom_commands[i])
    def read_prom(self, command):
        """
        Read a value from the PROM memory of the altimeter.
        Inputs:
            - command - hex command for which byte to read
        Returns int equal to value encoded at that memory slot
        """
        self._bus.write_byte_data(self._address, 0, command)
        time.sleep(0.05)
        data = self._bus.read_i2c_block_data(self._address, 0, 2)
        out = 0
        for i in range(2):
            out += data[i]*(2**(len(data)-i-1))
        return out
        
        
alt = Altimeter()
alt.initialize()
print(alt._c)