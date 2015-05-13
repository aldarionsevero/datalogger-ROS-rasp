from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import pyqtgraph as pg
from time import sleep
from datetime import datetime as dt
import logging
import random


class MainView(QDialog, QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.time_UI = 5
        # self.init_ui()
        self.plot()
        self.time = 0

    def build_logger(self, name):
        """ Method to build the logger's handler """
    # name = dt.strftime("%A, %d. %B %Y %I:%M%p")
        day = dt.now().strftime("%A, %d. %B %Y - %H_%M")
        from os import path

        root = path.dirname(path.abspath(__file__))
        handler = logging.FileHandler('%s/Logs/__%s.log' % (root, day))

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # define a logging format
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        return logger

    def update(self):
        global color, x, y, z
        a[0] = self.time + 1
        a[1] = random.randint(10, 200)
        loaded = "time:" + str(a[0]) + "temp:" + str(a[1])
        try:
            x.append(a[0])
            y.append(a[1])
            # z.append(a[2])
            print a
            logger.info(loaded)
        except IncompleteCaptureError:
            # print loaded
            pass
        except Exception, e:
            raise e

        # if len(x) > 100:
        x = x[1:]
        p.setData(x)

        if len(y) > 100:
            y = y[1:]
        q.setData(y)

        # if len(z) > 100:
        #    z = z[1:]
        # r.setData(z)
    def plot(self):
        logger = self.build_logger('plot')
        win = pg.GraphicsWindow()
        win.setWindowTitle('Scrolling Plots')

        x = range(10)
        y = range(10)
        plot_widgetx = win.addPlot()
        plot_widgetx.setRange(yRange=[0, 100])
        p = plot_widgetx.plot(x, y)

        win.nextRow()
        plot_widgety = win.addPlot()
        plot_widgety.setRange(yRange=[10, 200])
        q = plot_widgety.plot(x, y)

        # win.nextRow()
        # plotWidgetz = win.addPlot()
        # plotWidgetz.setRange(yRange=[300, 550])
        # r = plotWidgetz.plot(x, y)

        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(1)

    def init_ui(self):

        self.btn = QPushButton('Insert time', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.time_button)

        self.btn = QPushButton('START', self)
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
        pass
