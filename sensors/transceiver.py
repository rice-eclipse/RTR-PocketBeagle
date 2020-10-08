import digitalio
import board
import busio
import adafruit_rfm9x

"""
Must specify
- spi: SPI bus connected to radio
- cs: CS pin DigitalInOut
- reset: Reset pin DIO
--------------------------
Optional
- preamble_length: length in bytes of packet preamble
- high_power: Should be true
- baudrate: Baud rate of SPI connection

Notes: Made for compatibility with RadioHead Arduino, default packet header
is 4 bytes

Max sending is 252 bytes at time, not inclusive of 4 byte header
"""

radio_freq_mhz = 434.0
cs_pin = digitalio.DigitalInOut()
rst_pin = digitalio.DigitalInOut()
spi = busio.SPI("""boardSCK, MOSI, MISO""")
baudrate = 5000000
rfm9x = adafruit_rfm9x.RFM9X(spi, cs_pin, rst_pin, radio_freq_mhz, baudrate)


"""
data: data to be sent
keep_listening: send and receive?
destination: default dest for packet info, if 255 (0xff) then any recieving node
    will accept data, second byte of RadioHead header
node: If not 255 (0xff) then only packets address to this node will be accepted. 
    First byte of the RadioHead header. 

"""
data = "Coding is hard :C"
rfm9x.send(data, *, keep_listening, destination, node, identifier, flags)




