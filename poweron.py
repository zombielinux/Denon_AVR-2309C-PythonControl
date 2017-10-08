#!/bin/python
import pyserial

ser = serial.Serial(device='/dev/ttyUSB0',baudrate=9600)

ser.open()

ser.write(b'PWON\r')

ser.close()
