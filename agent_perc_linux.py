#!/bin/env python

import os
import platform
import socket
import time
import psutil
import json
import urllib2

last_disk_io  = psutil.disk_io_counters()
last_net_io   = psutil.net_io_counters()
time.sleep(1)

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def io_change(last, current):
    return dict([(f, getattr(current, f) - getattr(last, f))
                 for f in last._fields])

while True:

    memory          = psutil.phymem_usage()
    disk            = psutil.disk_usage("/")
    disk_io         = psutil.disk_io_counters()
    disk_io_change  = io_change(last_disk_io, disk_io)
    net_io          = psutil.net_io_counters()
    net_io_change   = io_change(last_net_io, net_io)
    last_disk_io    = disk_io
    last_net_io     = net_io

    gauges = {
        #"memory.used":        memory.used,
        #"memory.free":        memory.free,
        "sistema":             platform.system(),
        "versao_sistema":      platform.dist(),
        "hostname":           socket.gethostname(),
        "kernel":             platform.release(),
        "arquitetura":               platform.machine(), 
        #"ip":                 ip,
        #"uptime":             os.system("uptime"),
        "percentual_memoria":     memory.percent,
        "percentual_cpu":        psutil.cpu_percent(),
        "carga":               os.getloadavg()[0],
        #"disk.size.used":     disk.used,
        #"disk.size.free":     disk.free,
        "percentual_volume_disco":  disk.percent,
        #"disk.read.bytes":    disk_io_change["read_bytes"],
        #"disk.read.time":     disk_io_change["read_time"],
        #"disk.write.bytes":   disk_io_change["write_bytes"],
        #"disk.write.time":    disk_io_change["write_time"],
        #"net.in.bytes":       net_io_change["bytes_recv"],
        #"net.in.errors":      net_io_change["errin"],
        #"net.in.dropped":     net_io_change["dropin"],
        #"net.out.bytes":      net_io_change["bytes_sent"],
        #"net.out.errors":     net_io_change["errout"],
        #"net.out.dropped":    net_io_change["dropout"],
     }
    
    thresholds = {
        "percentual_memoria":     80,
        "percentual_volume_disco":  20,
        "percentual_cpu":        10,
        "carga":               0.10,
    }

    for name, bytes2human.value in gauges.items():
    	print name, bytes2human.value
        threshold = thresholds.get(name, None)
        if threshold is not None and bytes2human.value > threshold:
        	bits =(threshold, name)
        	message = "Limite de %s porcento foi atingido por %s" % bits
        	print message 
        	print "------------------"
    time.sleep(1)    	
