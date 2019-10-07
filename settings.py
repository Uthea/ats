# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settings_menu(object):
    def setupUi(self, settings_menu):
        settings_menu.setObjectName("settings_menu")
        settings_menu.setFixedSize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(settings_menu)
        self.buttonBox.setGeometry(QtCore.QRect(90, 240, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(settings_menu)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.algorithm = QtWidgets.QComboBox(settings_menu)
        self.algorithm.setGeometry(QtCore.QRect(250, 40, 111, 21))
        self.algorithm.setObjectName("algorithm")
        self.label_2 = QtWidgets.QLabel(settings_menu)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(settings_menu)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.language = QtWidgets.QComboBox(settings_menu)
        self.language.setGeometry(QtCore.QRect(250, 80, 111, 22))
        self.language.setObjectName("language")
        self.sen_count = QtWidgets.QLineEdit(settings_menu)
        self.sen_count.setGeometry(QtCore.QRect(250, 120, 113, 22))
        self.sen_count.setObjectName("sen_count")

        self.retranslateUi(settings_menu)
        self.buttonBox.accepted.connect(settings_menu.accept)
        self.buttonBox.rejected.connect(settings_menu.reject)
        QtCore.QMetaObject.connectSlotsByName(settings_menu)

    def retranslateUi(self, settings_menu):
        _translate = QtCore.QCoreApplication.translate
        settings_menu.setWindowTitle(_translate("settings_menu", "Settings"))
        self.label.setText(_translate("settings_menu", "Algorithm"))
        self.label_2.setText(_translate("settings_menu", "Sentence Count(Approx)"))
        self.label_3.setText(_translate("settings_menu", "Language"))


