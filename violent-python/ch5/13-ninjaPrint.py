#!/usr/bin/env python

import obexftp

try:
    btPrinter = obexftp.client(obexftp.BLUETOOTH)
    # Replace MAC with target MAC
    btPrinter.connect('00:11:22:33:44:55', 2)
    btPrinter.put_file('/tmp/ninja.jpg')
    print '[+] Printed Ninja Image.'
except:
    print '[-] Failed to print Ninja Image.'
