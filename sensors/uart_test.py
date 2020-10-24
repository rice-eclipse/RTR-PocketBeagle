import Adafruit_BBIO.UART as UART
import serial
import time
import Adafruit_BBIO.GPIO as GPIO

UART.setup("PB-UART1")#U0 Tx and Rx on PB
UART.setup("PB-UART2")#CLK and MOSI on SPI0

serB = serial.Serial(port = "/dev/ttyO2", baudrate = 9600)
serA = serial.Serial(port = "/dev/ttyO1", baudrate = 9600)

serA.close()
serB.close()
serB.open()
serA.open()

my_messages = ["what\n", "is\n", "love?\n"]

while True:
    serA.write("bee movie\n".encode('ascii'))
    serB.write("zee movie\n".encode('ascii'))
    time.sleep(1)
    print("Trying to check if serial is open")
    if serB.isOpen():
        print("Serial B is open")
    if serB.in_waiting > 0:
        print("Serial B is waiting")
    if serB.isOpen() and serB.in_waiting > 0:
        line = serB.readline().decode('ascii')
        print("the line is", line)
    time.sleep(0.1)