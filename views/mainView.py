from PyQt4.uic.Compiler.qtproxies import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import sleep


class MainView(QDialog, QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.time_UI = 5
        self.init_ui()

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
