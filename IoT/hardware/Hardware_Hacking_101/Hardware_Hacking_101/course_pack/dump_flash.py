#!/usr/bin/env python

import hexdump
import serial
import struct
from binascii import unhexlify


# Fix the values based on datasheet and hydrabus documentation
HB_MODE_SPI1 = '\xYY' # Set Hydrabus to SPI1 mode
HB_FREQUENCY = '\xYY' # Set Hydrabus to a frequency
NOR_ADDRESS = 0x # Set the address of the first Page to read from
NOR_SECTORS =  # Set the number of sectors on the NOR Flash
NOR_SECTOR_SIZE = # Set the NOR Flash sector size 

DEVICE = '' # Set USB device


#Open serial port
ser = serial.Serial(DEVICE, 115200)

#Open binary mode
for i in xrange(20):
	ser.write("\x00")
if "BBIO1" not in ser.read(5):
    print "Could not get into binary mode"
    quit()

# Switch to SPI mode
ser.write(HB_MODE_SPI1)
if "SPI" not in ser.read(4):
	print "Cannot set SPI mode"
	quit()

## Frequency 
ser.write('\x04\x00\x01\x00\x00')
ser.write(HB_FREQUENCY)
if ser.read(1):
	print "Frequency changed"


fout = open('/tmp/tplink.img', 'wb')


while(NOR_ADDRESS < NOR_SECTOR_SIZE * NOR_SECTORS):
		ser.write('\x04\x00\x04\x10\x00')
		ser.write('\x03' + unhexlify(hex(NOR_ADDRESS)[2:].zfill(6)))
		ser.read(1) # read Hydrabus status return
		buff = ser.read(NOR_SECTOR_SIZE)
		fout.write(buff)
		print "Reading address %x" % NOR_ADDRESS

		NOR_ADDRESS += NOR_SECTOR_SIZE

fout.close()


ser.write('\x00')
ser.write('\x0F\n')
