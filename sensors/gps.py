import Adafruit_BBIO.UART as UART
import serial
import pynmea2
import time
import Adafruit_BBIO.GPIO as GPIO


UART.setup("PB-UART0")

 
GPIO.setup("P8_12", GPIO.OUT)
GPIO.output("P8_12", GPIO.LOW)


ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600)
ser.close()
ser.open()

while(1):
    print("Trying to check if serial is open")
    if ser.isOpen():
        print("Serial is open")
    if ser.in_waiting:
        print("Serial is waiting")
    ser.write('t'.encode('utf-8'))
    if ser.isOpen() and ser.in_waiting:
        print("serial is open, reading the line")
        line = ser.readline()
        print("the line is {line}".format(line))
        if (line[0] == '$'):
            msg = pynmea2.parse(line)
            print(msg.lat_dir)
    time.sleep(1)
serial.close()
