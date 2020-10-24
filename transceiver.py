import digitalio
import board
import busio
import adafruit_rfm9x
import time
import adafruit_blinka.board.beagleboard.beaglebone_pocketbeagle
import Adafruit_BBIO

print(repr(Adafruit_BBIO))

print(repr(busio))

RADIO_FREQ_MHZ = 434.0

#CS and reset are correct (we checked with meters)
cs = digitalio.DigitalInOut(board.P2_31)
reset = digitalio.DigitalInOut(board.P2_8)
mypin = digitalio.DigitalInOut(board.P2_25)

"""
mypin.direction = digitalio.Direction.OUTPUT
mypin.value = False
print("Should be low right now")
time.sleep(1)
mypin.value = True
"""
print(repr(board))
print(repr(adafruit_blinka.board.beagleboard.beaglebone_pocketbeagle))
sck = board.SCLK_1#board.P2_29
mosi = board.MOSI_1#board.P2_25
miso = board.MISO_1#board.P2_27



spi = busio.SPI(sck, mosi, MISO=miso)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, RADIO_FREQ_MHZ, baudrate=9600)
print(rfm9x)
rfm9x.node = ord("t")
while True:
    packet = rfm9x.receive(keep_listening=True, with_header=True)
    #receive(*, keep_listening=True, with_header=False, with_ack=False, timeout=None)
    if packet is not None:
        print("Received a pak")
    else: 
        print("Packet was not recieved")
        print(packet)
    time.sleep(1)