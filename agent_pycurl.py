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

api_url = 'http://localhost:5000/api/v1.0/collector'

data = json.dumps({"arquitetura": "x64", "hostname": "hostname-test", "sistema": "linux", "done": "True"})

c = pycurl.Curl()
c.setopt(pycurl.URL, api_url)
c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json', 'Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()