# rpitempmonitor

Temperature Monitor for Raspberry PI using Adafruit PT100 (https://www.adafruit.com/product/3328).

The temperature is read out from MAX31865 with software SPI by using https://github.com/hackenbergstefan/MAX31865
and data is continously rendered using flask (http://flask.pocoo.org) as webserver providing data to highcharts (https://www.highcharts.com/) chart.
