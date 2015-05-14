#!/usr/bin/python
from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import pyqtgraph as pg
# from time import sleep
from datetime import datetime as dt
import logging
import random
import sys

inputs = [0, 0, 0, 0]
inputs_str = ['', '', '', '']

temperature = []
gas8 = []
gas9 = []


class MainView(QDialog, QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.delay_time = 0.02
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
        global color, temperature, gas8, gas9, inputs

        inputs[0] = random.randint(0, 100)
        inputs[1] = random.randint(0, 100)
        inputs[2] = random.randint(0, 100)
        # sleep(self.delay_time)

        inputs_str[0] = 'Temperature: ' + str(inputs[0])
        inputs_str[1] = 'Gas mq8: ' + str(inputs[1])
        inputs_str[2] = 'Gas mq9: ' + str(inputs[2])

        loaded = "temp: " + \
            str(inputs[0]) + " gas8: " + \
            str(inputs[1]) + " gas9: " + str(inputs[2])

        temperature.append(inputs[0])
        gas8.append(inputs[1])
        gas9.append(inputs[2])
        # print inputs
        self.logger.info(loaded)

        if len(temperature) > 100:
            temperature = temperature[1:]
        self.p.setData(temperature)

        self.lbl_temperature.setText(inputs_str[0])
        self.lbl_temperature.adjustSize()

        if len(gas8) > 100:
            gas8 = gas8[1:]
        self.q.setData(gas8)

        self.lbl_gas8.setText(inputs_str[1])
        self.lbl_gas8.adjustSize()

        if len(gas9) > 100:
            gas9 = gas9[1:]
        self.r.setData(gas9)

        self.lbl_gas9.setText(inputs_str[2])
        self.lbl_gas9.adjustSize()

        # if len(z) > 100:
        #    z = z[1:]
        # r.setData(z)
    def plot(self):
        self.build_logger('plot')
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('Scrolling Plots')

        temperature = range(10)
        gas8 = range(10)
        gas9 = range(10)

        plot_widget_temperature = self.win.addPlot()
        plot_widget_temperature.setRange(xRange=[0, 100])
        self.p = plot_widget_temperature.plot(temperature, gas8, gas9)

        self.win.nextRow()
        plot_widget_gas8 = self.win.addPlot()
        plot_widget_gas8.setRange(xRange=[0, 100])
        self.q = plot_widget_gas8.plot(temperature, gas8, gas9)

        self.win.nextRow()
        plot_widget_gas9 = self.win.addPlot()
        plot_widget_gas9.setRange(xRange=[0, 100])
        self.r = plot_widget_gas9.plot(temperature, gas8, gas9)

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

        self.lbl_gas8 = QtGui.QLabel(self)
        self.lbl_gas8.move(20, 60)

        self.lbl_gas9 = QtGui.QLabel(self)
        self.lbl_gas9.move(20, 100)

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

        self.delay_time, ok = QInputDialog.getDouble(self,
                                                     'Time',
                                                     'Enter the \
                                                      dealy time (s): ',
                                                     0.02,
                                                     decimals=2)
        if ok:
            print self.delay_time
            self.timer.setInterval(int(main_view.delay_time * 1000))

    def quit(self):
        exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.timer.timeout.connect(main_view.update)
    main_view.timer.start(int(main_view.delay_time * 1000))
    main_view.exec_()