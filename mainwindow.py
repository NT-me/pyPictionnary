# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 557)
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ani")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.motShower = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(50)
        self.motShower.setFont(font)
        self.motShower.setObjectName("motShower")
        self.verticalLayout.addWidget(self.motShower)
        self.Mot_Suivant = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setBold(True)
        font.setWeight(75)
        self.Mot_Suivant.setFont(font)
        self.Mot_Suivant.setObjectName("Mot_Suivant")
        self.verticalLayout.addWidget(self.Mot_Suivant)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.edit_List = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setBold(True)
        font.setWeight(75)
        self.edit_List.setFont(font)
        self.edit_List.setObjectName("edit_List")
        self.verticalLayout.addWidget(self.edit_List)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAfficher_pour_dition = QtWidgets.QAction(MainWindow)
        self.actionAfficher_pour_dition.setObjectName("actionAfficher_pour_dition")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pictionary"))
        self.Mot_Suivant.setText(_translate("MainWindow", "Mot Suivant"))
        self.edit_List.setText(_translate("MainWindow", "Editer liste"))
        self.actionAfficher_pour_dition.setText(_translate("MainWindow", "Afficher pour édition"))
