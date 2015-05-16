

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

# DS18B20 temperature sensor, digital output


from sensor import Sensor

from temp_DS18B20_read import DS18B20Read


class TempSensor(Sensor, DS18B20Read):

    """docstring for TempSensor"""

    def __init__(self):
        Sensor.__init__(self)
        self.sense_pin1 = 0  # pin 7 rasp
        self.gain = float(1 / 1000)
        # self.gain_plus = 150

    # def read_sensor(self):
    #     return self.read_pin(self.sense_pin1)

    # def read_new_gain(self):
    #     return self.read_gain_plus(self.gain_plus)
    def read_sensor(self):
        return self.temp_from_device
