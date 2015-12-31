#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Richardson Lima"
__copyright__ = "Copyright 2015, Python Infra DevOps Project"
__credits__ = ["",
                    ""]
__license__ = "GNU General Public License v2.0"
__version__ = "1.0.1"
__maintainer__ = "Richardson Lima"
__email__ = "contato@richardsonlima.com.br"
__status__ = "Test"

import pycurl, json
import os
import platform
import socket
import time
import psutil
import json
import urllib2

disk = psutil.disk_usage('/')
disk_total = disk.total / 2**30     # GiB.
disk_used = disk.used / 2**30
disk_free = disk.free / 2**30
disk_percent_used = disk.percent
cpu_usage = psutil.cpu_percent()
get_load = os.getloadavg()[0]
#ram = psutil.phymem_usage()
#ram_total = ram.total / 2**20       # MiB.
#ram_used = ram.used / 2**20
#ram_free = ram.free / 2**20
#ram_percent_used = ram.percent

process = psutil.Process(os.getpid())
print "[+] Platform: ",platform.system()
print "[+] Hostname: ",socket.gethostname()
#print "[+] Memory percent used: ",ram_percent_used
print "[+] CPU percent used: ",cpu_usage
print "[+] Disk percent used: ",disk_percent_used
print "[+] Load: ",os.getloadavg()[0]

api_url = 'http://api.domain:5000/api/v1/collector/add'

data = json.dumps({"sistema": platform.system(), "hostname": socket.gethostname(), "percentual_memoria":"ram_percent_used", "percentual_cpu": cpu_usage, "percentual_disco": disk_percent_used, "carga": get_load })

c = pycurl.Curl()
c.setopt(pycurl.URL, api_url)
c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json', 'Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
