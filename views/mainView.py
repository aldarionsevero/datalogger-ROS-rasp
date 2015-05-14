from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import pyqtgraph as pg
from time import sleep
from datetime import datetime as dt
import logging
import random

a = [0, 0]
x = []
y = []


class MainView(QDialog, QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.time_UI = 5
        self.init_ui()
        self.plot()
        self.time = 0

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
        global color, x, y, a
        a[0] = self.time + 1
        a[1] = random.randint(10, 200)
        loaded = "time:" + str(a[0]) + "temp:" + str(a[1])
        try:
            x.append(a[0])
            y.append(a[1])
            # z.append(a[2])
            print a
            self.logger.info(loaded)
        except Exception, e:
            raise e

        # if len(x) > 100:
        x = x[1:]
        self.p.setData(x)

        if len(y) > 100:
            y = y[1:]
        self.q.setData(y)

        # if len(z) > 100:
        #    z = z[1:]
        # r.setData(z)
    def plot(self):
        self.build_logger('plot')
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('Scrolling Plots')

        x = range(10)
        y = range(10)
        plot_widgetx = self.win.addPlot()
        plot_widgetx.setRange(yRange=[0, 100])
        self.p = plot_widgetx.plot(x, y)

        self.win.nextRow()
        plot_widgety = self.win.addPlot()
        plot_widgety.setRange(yRange=[10, 200])
        self.q = plot_widgety.plot(x, y)

        # win.nextRow()
        # plotWidgetz = win.addPlot()
        # plotWidgetz.setRange(yRange=[300, 550])
        # r = plotWidgetz.plot(x, y)

    def init_ui(self):

        self.btn = QPushButton('Insert time', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.time_button)

        self.btn = QPushButton('QUIT', self)
        self.btn.move(20, 80)
        self.btn.clicked.connect(self.start)

        self.setGeometry(600, 300, 300, 300)
        self.setWindowTitle('Videolaparoscopic')
        self.show()

    def time_button(self):

        self.time_UI, ok = QInputDialog.getInteger(self, 'Time',
                                                   '', 5)
        if ok:
            print self.time_UI

    def start(self):
        exit(0)
