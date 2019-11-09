# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mainwindow import Ui_MainWindow
import os
import sys
import random

def TxtToList(filename):
	"""
	Permet de transformer un fichier txt en une liste python
	"""
	res = []
	f = open(filename, "r")
	ligne=f.readline()
	while ligne !="":
		ligne=ligne.replace("\n","")
		res.append(ligne)
		ligne=f.readline()
	f.close()
	return res

class pyPict(QtWidgets.QMainWindow):
    def __init__(self, title="Default", parent=None):
        super(pyPict, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listeMots = TxtToList("listeMots.txt")
        self.ui.Mot_Suivant.clicked.connect(self.displayWord)
        self.ui.edit_List.clicked.connect(self.openListe)

    def displayWord(self):
        self.ui.motShower.clear()

        self.ui.motShower.append(random.choice(self.listeMots))

    def openListe(self):
        os.system('mousepad listeMots.txt')
        self.listeMots = TxtToList("listeMots.txt")
		


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = pyPict()
    w.show()
    sys.exit(app.exec_())
