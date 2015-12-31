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

from flask import Flask
from flask import g
from flask import Response
from flask import request
import json
import MySQLdb
import os

app = Flask(__name__)

@app.before_request
def db_connect():
  g.dbconn = MySQLdb.connect(host='127.0.0.1',
                              user='apiuser',
                              passwd='password',
                              db='api')
  g.cursor = g.dbconn.cursor()

@app.after_request
def db_disconnect(response):
  g.cursor.close()
  g.dbconn.close()
  return response

def query_db(query, args=(), one=False):
  g.cursor.execute(query, args)
  rv = [dict((g.cursor.description[idx][0], value)
  for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
  return (rv[0] if rv else None) if one else rv

@app.route("/")
def api():
  return "A Python API written with Flask Framework to collect servers health data."

@app.route("/api/v1/collector/view", methods=['GET'])
def view():
  result = query_db("SELECT sistema,hostname,percentual_memoria,percentual_cpu,percentual_disco,carga FROM api.servermonitor")
  data = json.dumps(result)
  resp = Response(data, status=200, mimetype='application/json')
  return resp

@app.route("/api/v1/collector/add", methods=['POST'])
def add():
  req_json = request.get_json()
  g.cursor.execute("INSERT INTO api.servermonitor (sistema, hostname, percentual_memoria, percentual_cpu, percentual_disco, carga) VALUES (%s,%s,%s,%s,%s,%s)", (req_json['sistema'], req_json['hostname'], req_json['percentual_memoria'], req_json['percentual_cpu'], req_json['percentual_disco'], req_json['carga']))
  g.dbconn.commit()
  resp = Response("Updated", status=201, mimetype='application/json')
  return resp

if __name__ == "__main__":
    # Bind to PORT ...
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
