# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Felipe\PycharmProjects\metacontrol\gui\views\ui_files\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 859)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainwindow/metacontrol_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabMainWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabMainWidget.sizePolicy().hasHeightForWidth())
        self.tabMainWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabMainWidget.setFont(font)
        self.tabMainWidget.setStyleSheet("QTabWidget::setTabIcon(0, QIcon(\'Screenshot.png\'))")
        self.tabMainWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabMainWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabMainWidget.setTabsClosable(False)
        self.tabMainWidget.setObjectName("tabMainWidget")
        self.simulationTab = QtWidgets.QWidget()
        self.simulationTab.setEnabled(True)
        self.simulationTab.setStyleSheet("")
        self.simulationTab.setObjectName("simulationTab")
        self.tabMainWidget.addTab(self.simulationTab, "")
        self.samplingTab = QtWidgets.QWidget()
        self.samplingTab.setEnabled(True)
        self.samplingTab.setObjectName("samplingTab")
        self.tabMainWidget.addTab(self.samplingTab, "")
        self.metamodelTab = QtWidgets.QWidget()
        self.metamodelTab.setEnabled(True)
        self.metamodelTab.setObjectName("metamodelTab")
        self.tabMainWidget.addTab(self.metamodelTab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setEnabled(True)
        self.tab_4.setObjectName("tab_4")
        self.tabMainWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setEnabled(True)
        self.tab_5.setObjectName("tab_5")
        self.tabMainWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabMainWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sampling/open_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sampling/save_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabMainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.simulationTab), _translate("MainWindow", "Load Simulation"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.samplingTab), _translate("MainWindow", "Sampling"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.metamodelTab), _translate("MainWindow", "Metamodel"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Opens a .mtc file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))

import icons_rc
