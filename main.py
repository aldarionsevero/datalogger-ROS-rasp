#!/usr/bin/python
from views.mainView import MainView

from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


def main():
    main_view = MainView()
    timer = QtCore.QTimer()
    timer.timeout.connect(main_view.update)
    timer.start(1)
    main_view.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
