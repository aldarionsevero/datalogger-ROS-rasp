# -*- coding: utf-8 -*-
# Copyright (c) 2015 "aldarionsevero Lucas Severo Alves
# <lucassalves65@gmail.com>""

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import botbook_gpio as gpio


class Sensor():  # Inherit from correct model to orm framework

    """docstring for Sensor"""

    sense_pin1 = 0
    sense_pin2 = 0
    sense_pin3 = 0
    sense_pin4 = 0
    sensor_level = 0
    gain = 1000
    gain_read = 0
    gain_plus = 0

    def __init__(self):
        self.sense_pin1 = 0
        self.sense_pin2 = 0
        self.sense_pin3 = 0
        self.sense_pin4 = 0
        self.sensor_level = 0

    def read_pin(self, pin):
        gpio.mode(pin, "in")
        gpio.interruptMode(pin, "both")
        return gpio.read(pin) * self.gain

    def read_gain_plus(self, plus):
        gain_read = self.gain + plus
        return gain_read
