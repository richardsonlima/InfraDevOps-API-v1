#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify, request, abort

app = Flask (__name__)

env = [
    {
        'id': 1,
        'sistema': u'',
        'versao_sistema': u'',
        'hostname': u'',
        'kernel': u'',
        'arquitetura': u'',
        'percentual_memoria': u'',
        'percentual_cpu': u'',
        'carga': u'',
        'percentual_volume_disco': u'',
        'done': False
    }

]

# Getting default
@app.route('/api/v1.0/collector', methods=['GET'])
def get_infra():
    return jsonify({'env': env})

# Getting by id

# Create a env obj
@app.route('/api/v1.0/collector', methods=['POST'])
def create_infra():
    if not request.json or not 'hostname' in request.json:
        abort(400)
    envs = {
        'id': env[-1]['id'] + 1,
        'sistema': request.json['sistema'],
        'versao_sistema': request.json.get('versao_sistema', ""),
        'hostname': request.json.get('hostname', ""),
        'kernel': request.json.get('kernel', ""),
        'arquitetura': request.json.get('arquitetura', ""),
        'percentual_memoria': request.json.get('percentual_memoria', ""),
        'percentual_cpu': request.json.get('percentual_cpu', ""),
        'percentual_volume_disco': request.json.get('percentual_volume_disco', ""),
        'carga': request.json.get('carga', ""),
        'done': False
    }
    env.append(envs)
    return jsonify({'envs': envs}), 201

if __name__ == '__main__':
    # Bind to PORT ...
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
