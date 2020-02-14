# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part-05.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 751, 371))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../../../../Pictures/Capture.PNG"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.image1Button = QtWidgets.QPushButton(self.centralwidget)
        self.image1Button.setGeometry(QtCore.QRect(120, 390, 75, 23))
        self.image1Button.setObjectName("image1Button")
        self.image2Button = QtWidgets.QPushButton(self.centralwidget)
        self.image2Button.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.image2Button.setObjectName("image2Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.image1Button.clicked.connect(self.show_image1)
        self.image2Button.clicked.connect(self.show_image2)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image1Button.setText(_translate("MainWindow", "Image 1"))
        self.image2Button.setText(_translate("MainWindow", "Image 2"))

    def show_image1(self):
        self.photo.setPixmap(QtGui.QPixmap("./image1.png"))

    def show_image2(self):
        self.photo.setPixmap(QtGui.QPixmap("./image2.jpg"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
