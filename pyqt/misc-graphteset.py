# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc-graphteset.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import pyqtgraph as pg
from pyqtgraph import BarGraphItem
import numpy as np
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 211, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.titleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")

        self.plotWidget = pg.plot()
        self.verticalLayout.addWidget(self.plotWidget)

        data = np.random.normal(size=(4,20))
        data[0] += 5
        data[1] += 7
        data[2] += 5
        data[3] = 10 + data[3] * 2

        self.barGraph = BarGraphItem(x=range(4), height=data.mean(axis=1), width = 0.3)
        self.plotWidget.addItem(self.barGraph)
        #subplot = self.mw.getFigure().addSubplot(111)


        self.verticalLayout.addWidget(self.titleLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        #self.plotWidget.addItem()
        #self.plotWidget.plot(hour, temperature, symbolpen='w')
        #self.plotWidget.plotItem()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(500)

    def update(self):
        data = np.random.normal(size=(4,20))
        data[0] += 5
        data[1] += 7
        data[2] += 5
        data[3] = 10 + data[3] * 2

        self.barGraph.setOpts(x=range(4), height=data.mean(axis=1), width = 0.3)
        self.plotWidget.plot()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
