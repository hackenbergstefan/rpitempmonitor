# /usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, render_template
from MAX31865.max31865 import MAX31865

app = Flask('rpitempmonitor')

max31865 = MAX31865(
    cs_pin=21,
    miso_pin=22,
    mosi_pin=23,
    clk_pin=24,
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temperature')
def temperature():
    return jsonify(temperature=max31865.temperature())


if __name__ == '__main__':
    with max31865:
        app.run(host='0.0.0.0', debug=True)
