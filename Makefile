all:
	pyuic5 mainwindow.ui > mainwindow.py
	python3 main.py
