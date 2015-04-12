#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import subprocess

filename = 'settings.json.example'
settings_file = 'settings.json'

with open(filename, 'r') as f:
    settings = json.loads(f.read(), encoding='UTF-8')

settings['redis']['host'] = os.environ['REDIS_PORT_6379_TCP_ADDR']
settings['redis']['port'] = os.environ['REDIS_PORT_6379_TCP_PORT']
settings['mongodb']['host'] = os.environ['MONGO_PORT_27017_TCP_ADDR']
settings['mongodb']['port'] = os.environ['MONGO_PORT_27017_TCP_PORT']

auth_default = os.environ.get('AUTH_DEFAULT')
if auth_default is not None:
    settings['auth']['default'] = auth_default

realm = os.environ.get('REALM')
if realm is not None:
    settings['realm'] = realm

with open(settings_file, 'w+') as f:
    f.write(json.dumps(settings))

# Add default user, ignore error when user already exists.
default_username = os.environ.get('DEFAULT_USERNAME', 'cantas')
default_password = os.environ.get('DEFAULT_PASSWORD', 'cantas')
cmd = ['node', 'scripts/addUser.js', default_username, default_password]
subprocess.call(cmd)

try:
    subprocess.call(['node', 'app.js'])
except KeyboardInterrupt:
    print 'Cantas ends'
