# rpitempmonitor

Temperature Monitor for Raspberry PI using Adafruit PT100 (https://www.adafruit.com/product/3328).

The temperature is read out from MAX31865 with software SPI by using https://github.com/hackenbergstefan/MAX31865
and data is continously rendered using flask (http://flask.pocoo.org) as webserver providing data to highcharts (https://www.highcharts.com/) chart.


## Intention

The original intention of this project is mastering the temperature of the coals of my barbecue.
Here are some images showing the rough setup and a recorded temperature curve.

![RaspberryPi Wiring](/doc/rpi.jpg)

![BBQ with temperature sensor](/doc/bbq.jpg)

![Example temperature curve](/doc/example_export.png)
