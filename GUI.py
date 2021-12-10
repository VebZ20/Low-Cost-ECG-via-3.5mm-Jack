# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 110, 201, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(370, 120, 61, 31))
        self.spinBox.setMaximum(9999)
        self.spinBox.setProperty("value", 40)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 130, 91, 16))
        self.label.setObjectName("label")
        self.grECG = PlotWidget(self.centralwidget)
        self.grECG.setGeometry(QtCore.QRect(10, 190, 1101, 591))
        self.grECG.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grECG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.grECG.setLineWidth(0)
        self.grECG.setObjectName("grECG")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(32, 20, 1071, 30))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setEnabled(True)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.btnSite = QtWidgets.QPushButton(self.frame_4)
        self.btnSite.setStyleSheet("color: rgb(0, 0, 255);")
        self.btnSite.setText("")
        self.btnSite.setCheckable(False)
        self.btnSite.setFlat(True)
        self.btnSite.setObjectName("btnSite")
        self.horizontalLayout_2.addWidget(self.btnSite)
        self.lblDevice = QtWidgets.QLabel(self.centralwidget)
        self.lblDevice.setEnabled(False)
        self.lblDevice.setGeometry(QtCore.QRect(30, 70, 1059, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lblDevice.setFont(font)
        self.lblDevice.setObjectName("lblDevice")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setGeometry(QtCore.QRect(470, 120, 121, 28))
        self.btnPause.setCheckable(True)
        self.btnPause.setObjectName("btnPause")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(610, 120, 131, 28))
        self.btnSave.setObjectName("btnSave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Low-cost ECG"))
        self.checkBox_2.setText(_translate("MainWindow", "Autoscale"))
        self.checkBox.setText(_translate("MainWindow", "Invert Signal"))
        self.spinBox.setToolTip(_translate("MainWindow", "set to 0 to disable"))
        self.spinBox.setSuffix(_translate("MainWindow", "Hz"))
        self.label.setText(_translate("MainWindow", "Lowpass Filter:"))
        self.label_4.setText(_translate("MainWindow", "ECG via 3.5mmJack"))
        self.label_5.setText(_translate("MainWindow", "   live soundcard monitor with realtime iFFT filtering by mi21mtech14004@iith.ac.in"))
        self.lblDevice.setText(_translate("MainWindow", "OOPS!!! Please check if there\'s a valid input connected. Kindly insert a 3.5 mm Jack and restart the program."))
        self.btnPause.setText(_translate("MainWindow", "Pause"))
        self.btnSave.setText(_translate("MainWindow", "Save ECG snap"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from pyqtgraph import PlotWidget
#import test1_rc
