#coding:utf-8
import serial
import time
import re

ser = serial.Serial("/dev/ttyAMA0", 115200)

dstAddr = raw_input("Please input the address:")
ser.write('AT+GETADDR')
time.sleep(0.1)
while True:
	count = ser.inWaiting()
	if count != 0:
	    myAddr = ser.read(count)
	    myAddr = re.findall("0x[0-9A-F]+", myAddr)
        myAddr = myAddr[0][2:]
	    print 'My address is %s' % myAddr
	    ser.flushInput()
        break

command = 'O2M 2 %s %s Hello, world!' % (myAddr, dstAddr)
ser.write(command)
time.sleep(0.1)
while True:
	count = ser.inWaiting()
	if count != 0:
	    myAddr = ser.read(count)
	    print myAddr
	    ser.flushInput()
        break

ser.close()

