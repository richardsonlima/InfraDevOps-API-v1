#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pycurl, json

api_url = 'http://localhost:5000/api/v1.0/collector'

data = json.dumps({"arquitetura": "x64", "hostname": "hostname-test", "sistema": "linux", "done": "True"})

c = pycurl.Curl()
c.setopt(pycurl.URL, api_url)
c.setopt(pycurl.HTTPHEADER, ['X-Postmark-Server-Token: API_TOKEN_HERE','Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()