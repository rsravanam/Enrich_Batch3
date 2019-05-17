#!/usr/bin/env python
from __future__ import print_function
import psutil
# gives a single float value
print ('cpu utilization:') 
# gives an object with many fields
#psutil.virtual_memory()
print(psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])
