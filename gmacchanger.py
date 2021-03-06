# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmachanger.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!



import os

if os.getuid() != 0:
    try:
        os.system("kdesu -d --noignorebutton -c \"python3 " + __file__ +"\"")
    except:
        try:
            os.system("gksu -k python3 " + __file__)
        except:
            try:
                os.system("ktsuss python3 " + __file__)
            except:
                os.system("konsole -e \"sudo python3 " + __file__ + '\"')
    exit()

from PyQt5 import QtCore, QtGui, QtWidgets
import macchangerfs
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 343)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(386, 343))
        MainWindow.setMaximumSize(QtCore.QSize(500, 343))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.radioButton_ending = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ending.setObjectName("radioButton_ending")
        self.gridLayout.addWidget(self.radioButton_ending, 9, 1, 1, 1)
        self.radioButton_another = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_another.setObjectName("radioButton_another")
        self.gridLayout.addWidget(self.radioButton_another, 8, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_permanent = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_permanent.setObjectName("pushButton_permanent")
        self.horizontalLayout_3.addWidget(self.pushButton_permanent)
        self.pushButton_setnew = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_setnew.setObjectName("pushButton_setnew")
        self.horizontalLayout_3.addWidget(self.pushButton_setnew)
        self.pushButton_info = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_info.sizePolicy().hasHeightForWidth())
        self.pushButton_info.setSizePolicy(sizePolicy)
        self.pushButton_info.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_info.setFont(font)
        self.pushButton_info.setText("")
        icon = QtGui.QIcon.fromTheme("help-about")
        self.pushButton_info.setIcon(icon)
        self.pushButton_info.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout_3.addWidget(self.pushButton_info)
        self.gridLayout.addLayout(self.horizontalLayout_3, 12, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_mac = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_mac.setObjectName("radioButton_mac")
        self.horizontalLayout_2.addWidget(self.radioButton_mac)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_customemacpre = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_customemacpre.setEnabled(False)
        self.comboBox_customemacpre.setMinimumSize(QtCore.QSize(85, 0))
        self.comboBox_customemacpre.setMaximumSize(QtCore.QSize(85, 16777215))
        self.comboBox_customemacpre.setAutoFillBackground(False)
        self.comboBox_customemacpre.setEditable(True)
        lista = macchangerfs.list()
        self.comboBox_customemacpre.addItems(lista[0][1] + lista[1][1])
        self.comboBox_customemacpre.setCurrentText("")
        self.comboBox_customemacpre.setObjectName("comboBox_customemacpre")
        self.horizontalLayout_4.addWidget(self.comboBox_customemacpre)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_customemac = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_customemac.setSizePolicy(sizePolicy)
        self.lineEdit_customemac.setMinimumSize(QtCore.QSize(70, 0))
        self.lineEdit_customemac.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_customemac.setMaxLength(8)
        self.lineEdit_customemac.setClearButtonEnabled(False)
        self.lineEdit_customemac.setObjectName("lineEdit_customemac")
        self.lineEdit_customemac.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.lineEdit_customemac)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.radioButton_random = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_random.setObjectName("radioButton_random")
        self.gridLayout.addWidget(self.radioButton_random, 10, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)
        self.label_addressinfo = QtWidgets.QLabel(self.centralWidget)
        self.label_addressinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_addressinfo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_addressinfo.setObjectName("label_addressinfo")
        self.gridLayout.addWidget(self.label_addressinfo, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_interfaces = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_interfaces.setObjectName("comboBox_interfaces")
        self.horizontalLayout.addWidget(self.comboBox_interfaces)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.checkBox_bia = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_bia.setEnabled(False)
        self.checkBox_bia.setObjectName("checkBox_bia")
        self.gridLayout.addWidget(self.checkBox_bia, 11, 1, 1, 1)
        self.radioButton_any = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_any.setObjectName("radioButton_any")
        self.gridLayout.addWidget(self.radioButton_any, 6, 1, 1, 1)
        self.comboBox_interfaces.addItems(macchangerfs.interfaces())
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.radioButton_random.toggled['bool'].connect(self.checkBox_bia.setEnabled)
        self.radioButton_mac.toggled['bool'].connect(self.comboBox_customemacpre.setEnabled)
        self.radioButton_mac.toggled['bool'].connect(self.lineEdit_customemac.setEnabled)
        self.pushButton_permanent.clicked.connect(self.click_permanent)
        self.pushButton_setnew.clicked.connect(self.click_setnew)
        self.pushButton_info.clicked.connect(self.click_version)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gmacchanger"))
        self.label_3.setText(_translate("MainWindow", "Set MAC"))
        self.radioButton_ending.setText(_translate("MainWindow", "Don\'t change the vendor bytes"))
        self.radioButton_another.setText(_translate("MainWindow", "Set random vendor MAC of the same kind"))
        self.pushButton_permanent.setText(_translate("MainWindow", "Reset to permanent MAC"))
        self.pushButton_setnew.setText(_translate("MainWindow", "Set new MAC"))
        self.radioButton_mac.setText(_translate("MainWindow", "Set the MAC to"))
        self.comboBox_customemacpre.lineEdit().setPlaceholderText(_translate("MainWindow", "XX:XX:XX"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.lineEdit_customemac.setPlaceholderText(_translate("MainWindow", "XX:XX:XX"))
        self.radioButton_random.setText(_translate("MainWindow", "Set fully random MAC"))
        self.label_addressinfo.setText(_translate("MainWindow", "Current MAC:\nPermanent MAC:"))
        self.label.setText(_translate("MainWindow", "Select interface"))
        self.checkBox_bia.setText(_translate("MainWindow", "Pretend to be a burned-in-address"))
        self.radioButton_any.setText(_translate("MainWindow", "Set random vendor MAC of any kind"))

    def click_setnew(self):
        if self.radioButton_mac.isChecked():
            macchangerfs.mac(device=self.comboBox_interfaces.currentText(), mac=self.comboBox_customemacpre.currentText() + ':' + self.lineEdit_customemac.text())
        elif self.radioButton_ending.isChecked():
            macchangerfs.ending(device=self.comboBox_interfaces.currentText())
        elif self.radioButton_another.isChecked():
            macchangerfs.another(device=self.comboBox_interfaces.currentText())
        elif self.radioButton_any.isChecked():
            macchangerfs.Any(device=self.comboBox_interfaces.currentText())
        elif self.radioButton_random.isChecked():
            macchangerfs.random(device=self.comboBox_interfaces.currentText(), bia=True if self.checkBox_bia.isChecked() else False)

    def click_permanent(self):
        macchangerfs.permanent(device=self.comboBox_interfaces.currentText())

    def click_version(self):
        #QtWidgets.QMessageBox.about(QtWidgets.QWidget(), "Info", macchangerfs.version())
        QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "Info", macchangerfs.version())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Breeze Dark")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def update_label():
        ui.label_addressinfo.setText(macchangerfs.show(device=ui.comboBox_interfaces.currentText()))

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(100)

    sys.exit(app.exec_())
