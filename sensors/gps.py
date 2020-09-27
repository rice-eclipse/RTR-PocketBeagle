import Adafruit_BBIO.UART as UART
import serial
import pynmea2
import time
import Adafruit_BBIO.GPIO as GPIO


UART.setup("PB-UART0")

 
GPIO.setup("P1_35", GPIO.OUT)
GPIO.output("P1_35", GPIO.LOW)

GPIO.setup("P1_34", GPIO.IN)

#GPIO.setup("", )

ser = serial.Serial(port = "/dev/ttyO0", baudrate=9600)
ser.close()
ser.open()

while(1):
    if GPIO.input("P1_34"):
        print("HIGH")
    else:
        print("LOW")

    print("Trying to check if serial is open")
    if ser.isOpen():
        #ser.write(("$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47\r\n").encode('utf-8'))
        print("Serial is open")
    if ser.inWaiting():
        print("Serial is waiting")
    ser.write('t'.encode('utf-8'))
    if ser.isOpen() and ser.inWaiting():
        print("serial is open, reading the line")
        line = ser.read()
        print("the line is {line}".format(line))
        if (line[0] == '$'):
            msg = pynmea2.parse(line)
            print(msg.lat_dir)
    time.sleep(1)
serial.close()
