import digitalio
import board
import busio
import adafruit_rfm9x

print(repr(board))

RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.P2_11)
RESET = digitalio.DigitalInOut(board.P2_24)
spi = busio.SPI(board.SCK_0, MOSI=board.MOSI_0, MISO=board.MISO_0)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)