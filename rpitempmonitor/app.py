# /usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
from flask import Flask, jsonify, render_template
from datalogger import DataLogger
try:
    from MAX31865.max31865 import MAX31865
except ModuleNotFoundError:
    from max31865mock import MAX31865

app = Flask('rpitempmonitor')
"""Flask-App reflecting this website."""

max31865 = MAX31865(
    cs_pin=21,
    miso_pin=22,
    mosi_pin=23,
    clk_pin=24,
)
"""Interface to MAX31865."""

datalogger = None
"""DataLogger to save logged temperature to file."""


@app.route('/')
def index():
    global datalogger
    datalogger = DataLogger('data_%d.csv' % int(time.time()))
    return render_template('index.html')


@app.route('/<logged_data>')
def data(logged_data):
    if not os.path.exists(logged_data):
        return '<br/>'.join(os.listdir('.'))
    data = DataLogger(logged_data).read()
    start_time = float(data[0][0])
    data = [[float(a) - start_time, float(b)] for a, b in data]
    return render_template('data.html', data=data, data_filename=logged_data)


@app.route('/temperature')
def temperature():
    temp = max31865.temperature()
    datalogger.add_data((time.time(), temp))
    return jsonify(temperature=temp)


if __name__ == '__main__':
    with max31865:
        app.run(host='0.0.0.0', debug=True)
