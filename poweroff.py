#!/bin/python3
import pyserial

ser = serial.Serial(device='/dev/ttyUSB0',baudrate=9600)

ser.open()

ser.write(b'PWSTANDBY\r')

ser.close()
