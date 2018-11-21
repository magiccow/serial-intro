#!/usr/bin/env python

import time
import serial


ser = serial.Serial(
           port='/dev/ttyAMA0',
           baudrate = 9600,
           timeout=1
   )

counter=0

while 1:
        bytesToRead = ser.inWaiting()
        if bytesToRead>2:
                data = ser.read()
                print(data)
