import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt
import design

class MainApp(QMainWindow, design.Ui_MainWindow):
	resized = QtCore.pyqtSignal()
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.resized.connect(self.on_mwresize)
		self.show()
		self.attempt = [0,False]

	def stickman_update(self):
		pass

	def resizeEvent(self,event):
		self.resized.emit()
		return super(MainApp, self).resizeEvent(event)
	def on_mwresize(self):
		if self.geometry().height() < 642:
			self.verticalFrame_2.setHidden(True)
		elif self.geometry().height() >= 642:
			self.verticalFrame_2.setHidden(False)
if __name__ == "__main__":

	app = QApplication(sys.argv)
	ex = MainApp()
	sys.exit(app.exec_())
