# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import summarizer
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 1021, 441))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 570, 391, 81))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 311, 51))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1061, 721))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 110, 1021, 311))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 321, 71))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 500, 501, 111))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(220, 248, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1071, 721))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 471, 411))
        self.label_3.setStyleSheet("border : 2px solid red;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(570, 80, 471, 411))
        self.label_5.setStyleSheet("border : 2px solid red;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 31))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionSummarizer = QtWidgets.QAction(MainWindow)
        self.actionSummarizer.setObjectName("actionSummarizer")
        self.actionVisualization = QtWidgets.QAction(MainWindow)
        self.actionVisualization.setObjectName("actionVisualization")
        self.menuHome.addAction(self.actionHome)
        self.menuHome.addAction(self.actionSummarizer)
        self.menuHome.addAction(self.actionVisualization)
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Summarize"))
        self.label.setText(_translate("MainWindow", "Text Summarizer"))
        self.label_2.setText(_translate("MainWindow", "Summarized Text"))
        self.pushButton_2.setText(_translate("MainWindow", "Visualize Summary"))
        self.menuHome.setTitle(_translate("MainWindow", "Options"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionSummarizer.setText(_translate("MainWindow", "Summarizer"))
        self.actionVisualization.setText(_translate("MainWindow", "Visualization"))

        self.frame.hide()
        self.pushButton.clicked.connect(self.showSummarizer)
        self.pushButton_2.clicked.connect(self.showVisualization)

        self.actionHome.triggered.connect(self.showHome)

    def showHome(self):
        self.frame.hide()

    def showSummarizer(self):
        self.frame.show()
        self.frame_2.hide()

        text = self.textEdit.toPlainText()
        pred = summarizer.predict(text)
        self.textEdit_3.setText(pred)

    def showVisualization(self):
        self.frame_2.show()

        self.img_1 = QtGui.QPixmap('plot1.png')
        self.img_1 = self.img_1.scaledToHeight(self.label_3.height())
        self.img_1 = self.img_1.scaledToWidth(self.label_3.width())
        self.label_3.setPixmap(self.img_1)

        self.img_2 = QtGui.QPixmap('plot2.png')
        self.img_2 = self.img_2.scaledToHeight(self.label_5.height())
        self.img_2 = self.img_2.scaledToWidth(self.label_5.width())
        self.label_5.setPixmap(self.img_2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
