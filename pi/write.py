#!/usr/bin/env python

import serial


ser = serial.Serial(
           port='/dev/ttyAMA0',
           baudrate = 9600,
           timeout=1
   )


ser.write('CCC')


