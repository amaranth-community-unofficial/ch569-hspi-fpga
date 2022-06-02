#!/usr/bin/env python3
import usb
from luna.gateware.usb.devices.ila  import USBIntegratedLogicAnalyzerFrontend
from amlib.debug.ila                import ILACoreParameters


dev=usb.core.find(idVendor=0x1209, idProduct=0x4711)
print(dev)

frontend = USBIntegratedLogicAnalyzerFrontend(ila=ILACoreParameters.unpickle(), idVendor=0x1209, idProduct=0x4711, endpoint_no=1)
frontend.interactive_display()
