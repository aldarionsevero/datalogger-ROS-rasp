#!/usr/bin/python

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

from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from sensors.temp_sensor import TempSensor
from sensors.mq9_sensor import Mq9Sensor
from sensors.mq135_sensor import Mq135Sensor

import pyqtgraph as pg
# from time import sleep
from datetime import datetime as dt
import logging
import random
import sys
import optparse
from time import sleep

inputs = [0, 0, 0, 0]
inputs_str = ['', '', '', '']


temp_sensor = TempSensor()
mq9_sensor = Mq9Sensor()
mq135_sensor = Mq135Sensor()

temperature = []
gas135 = []
gas8 = []
gas9 = []


class MainView(QDialog, QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.delay_time = 0.08
        self.main_menu()

        self.timer = QtCore.QTimer()
        self.plot()

    def build_logger(self, name):
        """ Method to build the logger's handler """
    # name = dt.strftime("%A, %d. %B %Y %I:%M%p")
        day = dt.now().strftime("%A, %d. %B %Y - %H_%M")
        from os import path

        root = path.dirname(path.abspath(__file__))
        handler = logging.FileHandler('%s/Logs/__%s.log' % (root, day))

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # define a logging format
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(handler)

    def update(self):
        global color, temperature, gas135, gas8, gas9, inputs

        inputs[0] = temp_sensor.read_sensor()
        inputs[1] = mq135_sensor.read_sensor()
        # inputs[2] = mq8_sensor.read_sensor()
        # inputs[3] = mq9_sensor.read_sensor()

        # inputs[0] = random.randint(0, 100)
        # inputs[1] = random.randint(0, 100)
        # inputs[2] = random.randint(0, 100)
        # inputs[3] = random.randint(0, 100)

        inputs_str[0] = 'Temperature: ' + str(inputs[0])
        inputs_str[1] = 'Gas mq135: ' + str(inputs[1])
        inputs_str[2] = 'Gas mq8: ' + str(inputs[2])
        inputs_str[3] = 'Gas mq9: ' + str(inputs[3])

        loaded = "temp: " + \
            str(inputs[0]) + " gas135: " + \
            str(inputs[1]) + " gas8: " + \
            str(inputs[2]) + " gas9: " + str(inputs[3])

        temperature.append(inputs[0])
        gas135.append(inputs[1])
        gas8.append(inputs[2])
        gas9.append(inputs[3])
        # print inputs
        self.logger.info(loaded)

        if len(temperature) > 100:
            temperature = temperature[1:]
        self.p.setData(temperature)

        self.lbl_temperature.setText(inputs_str[0])
        self.lbl_temperature.adjustSize()

        if len(gas135) > 100:
            gas135 = gas135[1:]
        self.q.setData(gas135)

        self.lbl_gas135.setText(inputs_str[1])
        self.lbl_gas135.adjustSize()

        # if len(gas8) > 100:
        #     gas8 = gas8[1:]
        # self.r.setData(gas8)

        # self.lbl_gas8.setText(inputs_str[2])
        # self.lbl_gas8.adjustSize()

        # if len(gas9) > 100:
        #     gas9 = gas9[1:]
        # self.s.setData(gas9)

        self.lbl_gas9.setText(inputs_str[3])
        self.lbl_gas9.adjustSize()

        # if len(z) > 100:
        #    z = z[1:]
        # r.setData(z)

    def plot(self):
        self.build_logger('plot')
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('Drone Datalogger')

        temperature = range(10)
        gas135 = range(10)
        gas8 = range(10)
        gas9 = range(10)

        plot_widget_temperature = self.win.addPlot()
        plot_widget_temperature.setRange(xRange=[0, 100])
        self.p = plot_widget_temperature.plot(temperature, gas135, gas8, gas9)

        self.win.nextRow()
        plot_widget_gas135 = self.win.addPlot()
        plot_widget_gas135.setRange(xRange=[0, 100])
        self.q = plot_widget_gas135.plot(temperature, gas135, gas8, gas9)

        # self.win.nextRow()
        # plot_widget_gas8 = self.win.addPlot()
        # plot_widget_gas8.setRange(xRange=[0, 100])
        # self.r = plot_widget_gas8.plot(temperature, gas135, gas8, gas9)

        # self.win.nextRow()
        # plot_widget_gas9 = self.win.addPlot()
        # plot_widget_gas9.setRange(xRange=[0, 100])
        # self.s = plot_widget_gas9.plot(temperature, gas135, gas8, gas9)

        # win.nextRow()
        # plotWidgetz = win.addPlot()
        # plotWidgetz.setRange(yRange=[300, 550])
        # r = plotWidgetz.plot(temperature, gas8)

    # def choose_sensor(self):

    def main_menu(self):

        # self.combo = QtGui.QComboBox(self)
        # self.combo.addItem("Temperature")
        # self.combo.addItem("Gas mq8")
        # self.combo.addItem("Gas mq9")
        # self.combo.addItem("All")
        # self.combo.move(20, 20)
        # print str(self.combo.currentText())

        self.lbl_temperature = QtGui.QLabel(self)
        self.lbl_temperature.move(20, 20)

        self.lbl_gas135 = QtGui.QLabel(self)
        self.lbl_gas135.move(20, 60)

        # self.lbl_gas8 = QtGui.QLabel(self)
        # self.lbl_gas8.move(20, 100)

        # self.lbl_gas9 = QtGui.QLabel(self)
        # self.lbl_gas9.move(20, 140)

        self.btn = QPushButton('Delay Time', self)
        self.btn.move(20, 250)
        self.btn.clicked.connect(self.set_delay)

        self.btn = QPushButton('Quit', self)
        self.btn.move(180, 250)
        self.btn.clicked.connect(self.quit)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Data Logger')
        self.show()

    def set_delay(self):

        self.delay_time, ok = QInputDialog.getDouble(self, 'Time',
                                                     'Enter the dealy \
                                                     time (s): ',
                                                     0.08,
                                                     decimals=2)
        if ok:
            print self.delay_time
            self.timer.setInterval(int(main_view.delay_time * 1000))

    def quit(self):
        exit(0)

# TODO take this out of this file... make is work


class Terminal(object):

    """docstring for Terminal"""

    delay_time = 0.08
    logger = logging.getLogger(__name__)

    def __init__(self):
        super(Terminal, self).__init__()
        self.print_sensor_readings()

    def build_logger(self, name):
        """ Method to build the logger's handler """
    # name = dt.strftime("%A, %d. %B %Y %I:%M%p")
        day = dt.now().strftime("%A, %d. %B %Y - %H_%M")
        from os import path

        root = path.dirname(path.abspath(__file__))
        handler = logging.FileHandler('%s/Logs/__%s.log' % (root, day))

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # define a logging format
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(handler)

    def print_sensor_readings(self):
        while 1:
            self.build_logger('plot')
            global color, temperature, gas135, gas8, gas9, inputs

            inputs[0] = temp_sensor.read_sensor()
            inputs[1] = mq135_sensor.read_sensor()
            # inputs[2] = mq8_sensor.read_sensor()
            # inputs[3] = mq9_sensor.read_sensor()

            # inputs[0] = random.randint(0, 100)
            # inputs[1] = random.randint(0, 100)
            # inputs[2] = random.randint(0, 100)
            # inputs[3] = random.randint(0, 100)

            inputs_str[0] = 'Temperature: ' + str(inputs[0])
            inputs_str[1] = 'Gas mq135: ' + str(inputs[1])
            inputs_str[2] = 'Gas mq8: ' + str(inputs[2])
            inputs_str[3] = 'Gas mq9: ' + str(inputs[3])

            loaded = "temp: " + \
                str(inputs[0]) + " gas135: " + \
                str(inputs[1]) + " gas8: " + \
                str(inputs[2]) + " gas9: " + str(inputs[3])

            temperature.append(inputs[0])
            gas135.append(inputs[1])
            gas8.append(inputs[2])
            gas9.append(inputs[3])
            # print inputs
            self.logger.info(loaded)

            if len(temperature) > 100:
                temperature = temperature[1:]

            if len(gas135) > 100:
                gas135 = gas135[1:]

            if len(gas8) > 100:
                gas8 = gas8[1:]

            if len(gas9) > 100:
                gas9 = gas9[1:]

            print inputs_str
            sleep(self.delay_time)


if __name__ == '__main__':
    sys.stdout.flush()
    parser = optparse.OptionParser(
        usage="%prog [options]",
        description="Datalogger"
    )
    parser.add_option("-t", "--terminal",
                      dest="terminal",
                      action="store_true",
                      help="Runs on terminal only",
                      default=False
                      )
    (options, args) = parser.parse_args()
    if options.terminal:
        tm = Terminal()
    else:
        app = QApplication(sys.argv)
        main_view = MainView()
        main_view.timer.timeout.connect(main_view.update)
        main_view.timer.start(int(main_view.delay_time * 1000))
        main_view.exec_()
