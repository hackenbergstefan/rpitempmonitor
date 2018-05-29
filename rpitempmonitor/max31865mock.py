# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mock of MAX31865 to test and run rpitempmonitor on non-Rpi environment.
"""

import random


class MAX31865(object):

    def __init__(self, *k, **kw):
        pass

    def temperature(self):
        """
        Read out temperature.
        For this mock just return random number.
        """
        return random.randint(0, 500)

    def __enter__(self):
        return self

    def __exit__(self, *k):
        pass
