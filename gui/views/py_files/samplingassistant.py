# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Felipe\metacontrol\gui\views\ui_files\samplingassistant.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(1063, 657)
        Dialog.setMinimumSize(QtCore.QSize(1000, 600))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    top: 5px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.genLhsPushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.genLhsPushButton.setEnabled(True)
        self.genLhsPushButton.setObjectName("genLhsPushButton")
        self.horizontalLayout_2.addWidget(self.genLhsPushButton)
        self.lhsSettingsPushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.lhsSettingsPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sampling/settings_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lhsSettingsPushButton.setIcon(icon)
        self.lhsSettingsPushButton.setObjectName("lhsSettingsPushButton")
        self.horizontalLayout_2.addWidget(self.lhsSettingsPushButton)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.genRectGridPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.genRectGridPushButton.setObjectName("genRectGridPushButton")
        self.gridLayout_3.addWidget(self.genRectGridPushButton, 0, 0, 1, 1)
        self.rectGridSettingspushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.rectGridSettingspushButton.setText("")
        self.rectGridSettingspushButton.setIcon(icon)
        self.rectGridSettingspushButton.setObjectName("rectGridSettingspushButton")
        self.gridLayout_3.addWidget(self.rectGridSettingspushButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 8)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    top: 5px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.displayProgressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.displayProgressBar.setProperty("value", 0)
        self.displayProgressBar.setObjectName("displayProgressBar")
        self.gridLayout_4.addWidget(self.displayProgressBar, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        self.cancelPushButton = QtWidgets.QPushButton(Dialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.gridLayout.addWidget(self.cancelPushButton, 5, 7, 1, 1)
        self.donePushButton = QtWidgets.QPushButton(Dialog)
        self.donePushButton.setObjectName("donePushButton")
        self.gridLayout.addWidget(self.donePushButton, 5, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 4, 1, 1)
        self.sampDataPushButton = QtWidgets.QPushButton(Dialog)
        self.sampDataPushButton.setEnabled(False)
        self.sampDataPushButton.setObjectName("sampDataPushButton")
        self.gridLayout.addWidget(self.sampDataPushButton, 5, 5, 1, 1)
        self.exportCsvPushButton = QtWidgets.QPushButton(Dialog)
        self.exportCsvPushButton.setEnabled(False)
        self.exportCsvPushButton.setObjectName("exportCsvPushButton")
        self.gridLayout.addWidget(self.exportCsvPushButton, 5, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.abortSamplingPushButton = QtWidgets.QPushButton(Dialog)
        self.abortSamplingPushButton.setEnabled(False)
        self.abortSamplingPushButton.setObjectName("abortSamplingPushButton")
        self.gridLayout.addWidget(self.abortSamplingPushButton, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 9px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    top: 5px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.tableViewInputVariables = QtWidgets.QTableView(self.groupBox_4)
        self.tableViewInputVariables.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableViewInputVariables.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewInputVariables.setObjectName("tableViewInputVariables")
        self.tableViewInputVariables.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.tableViewInputVariables, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 7)

        self.retranslateUi(Dialog)
        self.radioButton.toggled['bool'].connect(self.groupBox_6.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.groupBox_2.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sampling Assistant"))
        self.genLhsPushButton.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"justify\">Generates the Latin Hypercube Sampling (LHS) when <span style=\" text-decoration: underline;\">all</span> the manipulated variables have their lower and upper bounds defined. Default number of points is 10 * number of variables. To change this, click on the settings button.</p></body></html>"))
        self.genLhsPushButton.setText(_translate("Dialog", "Generate LHS"))
        self.lhsSettingsPushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Latin Hypercube Sampling (LHS) settings</p></body></html>"))
        self.genRectGridPushButton.setText(_translate("Dialog", "Generate Grid"))
        self.radioButton_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Method to be implemented in the future</p></body></html>"))
        self.radioButton_2.setText(_translate("Dialog", "Regular Grid"))
        self.radioButton.setText(_translate("Dialog", "Latin Hypercube Sampling (LHS)"))
        self.label.setText(_translate("Dialog", "Select a sampling method"))
        self.label_2.setText(_translate("Dialog", "Sampler display"))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel"))
        self.donePushButton.setText(_translate("Dialog", "Done"))
        self.sampDataPushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Query the simulation engine to sample the model. May take a while depending on model complexity and number of samples.</p></body></html>"))
        self.sampDataPushButton.setText(_translate("Dialog", "Sample Data"))
        self.exportCsvPushButton.setText(_translate("Dialog", "Export as CSV"))
        self.abortSamplingPushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Aborts the sampling</p></body></html>"))
        self.abortSamplingPushButton.setText(_translate("Dialog", "Abort"))
        self.label_3.setText(_translate("Dialog", "Bounds definition"))

from gui.resources import icons_rc
