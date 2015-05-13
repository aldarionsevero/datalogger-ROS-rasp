#!/usr/bin/python
from views.mainView import MainView

from PyQt4.uic.Compiler.qtproxies import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


def main():
    main_view = MainView()
    main_view.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
