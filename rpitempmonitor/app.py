# /usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask

app = Flask('rpitempmonitor')


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
