#!/usr/bin/env python

from bluetooth import *


def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print '[+] RFCOMM Port ' + str(port) + ' open'
        sock.close()
    except Exception, e:
        print '[-] RFCOMM Port ' + str(port) + ' closed'


for port in range(1, 30):
    # Replace MAC with target MAC
    rfcommCon('00:11:22:33:44:55', port)
