import Adafruit_BBIO.UART as UART
import serial
import time
import Adafruit_BBIO.GPIO as GPIO

UART.setup("PB-UART0")#U0 Tx and Rx on PB
UART.setup("PB-UART2")#CLK and MOSI on SPI0

serA = serial.Serial(port = "/dev/ttyO0", baudrate = 9600)
serB = serial.Serial(port = "/dev/ttyO2", baudrate = 9600)

serA.close()
serB.close()
serB.open()
serA.open()

my_messages = ["what\r", "is\n", "love?\n"]

for i in range(len(my_messages)):
    serA.write(my_messages[i].encode('ascii'))
    time.sleep(1)
    print("Trying to check if serial is open")
    if serB.isOpen():
        print("Serial is open")
    if serB.in_waiting:
        print("Serial is waiting")
    if serB.isOpen() and serB.in_waiting > 0:
        line = serB.readline().decode('ascii')
        print("the line is", line)
    time.sleep(1)