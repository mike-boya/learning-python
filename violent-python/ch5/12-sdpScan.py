#!/usr/bin/env python

from bluetooth import *


def sdpBrowse(addr):
    services = find_service(address=addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print '[+] Found ' + str(name) + ' on ' + str(proto) + ':' + port

# Replace MAC with target
sdpBrowse('00:11:22:33:44:55')
