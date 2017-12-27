#!/usr/bin/env python

import sys
import struct
import volatility.conf as conf
import volatility.registry as registry
import volatility.commands as commands
import volatility.addrspace as addrspace
from volatility.plugins.registry.registryapi import RegistryApi
from volatility.plugins.registry.lsadump import HashDump

memory_file = "WIN7SP1.raw"
sys.path.append("/usr/lib/python2.7/dist-packages/volatility/")

registry.PluginImporter()
config = conf.ConfObject()

config.parse_options()
config.PROFILE  = "Win7SP1x64"
config.LOCATION = "file://%s" % memory_file

registry.register_global_options(config, commands.Command)
registry.register_global_options(config, addrspace.BaseAddressSpace)

registry = RegistryApi(config)
registry.populate_offsets()

sam_offset = None
sys_offset = None

for offset in registry.all_offsets:

    if registry.all_offsets[offset].endswith("\\SAM"):
        sam_offset = offset
        print "[*] SAM: 0x%08x" % offset
    # modified case on system for Win7
    if registry.all_offsets[offset].endswith("\\SYSTEM"):
        sys_offset = offset
        print "[*] SYSTEM: 0x%08x" % offset
    if sam_offset is not None and sys_offset is not None:
        config.sys_offset = sys_offset
        config.sam_offset = sam_offset
        hashdump = HashDump(config)
        for hash in hashdump.calculate():
            print hash
        break

if sam_offset is None or sys_offset is None:
    print "[*] Failed to find the SYSTEM or SAM offsets."
