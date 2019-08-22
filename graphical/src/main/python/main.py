from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from PyQt5.QtCore import Qt
import parser, design, sys, requests, random

class MainApp(QMainWindow, design.Ui_MainWindow):
	resized = QtCore.pyqtSignal()
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.auto_add = True
		self.resized.connect(self.on_mwresize)
		self.show()
		self.appctxt = ApplicationContext()
		self.setListener()
		self.attempt = [1,False]
		try:
			a = parser.RandomRightWord()
			self.word = a.get_word()
		except requests.exceptions.ConnectionError:
			try:
				a = parser.RandomWord()
				self.word = a.get_word()
			except requests.exceptions.ConnectionError:
				with open(self.appctxt.get_resource('dictionary.txt'), 'r') as f:
					f = f.read().split('\n')
					for x in range(len(f)-1, -1, -1):
						if f[x]=='':
							del f[x]
					random.shuffle(f)
					word = f[0].split('||')
					self.word = {'word': word[0], 'description': word[1]}
			except FileNotFoundError:
				QMessageBox.warning(self, "Error",
				"Connect to internet or make dictionary in the program's resource folder")
				return
		if self.auto_add:
			with open("dictionary.txt", 'a') as f:
				f.write(word['word']+"||"+word['description'])
		self.answered = ['_' for x in self.word['word']]
		self.logic()
		self.prev = []

	def stickman_update(self):
		self.label_4.setPixmap(QPixmap(self.appctxt.get_resource(f'Man {str(self.attempt[0])}|{str(int(self.attempt[1]))}.svg')))

	def logic(self, letter=None):
		if type(letter) != str:
			pass
		else:
			letter = letter.lower()
			right = False
			for x in range(0,len(self.word['word'])):
				if letter == self.word['word'][x]:
					self.answered[x] = letter
					right = True
			if letter.upper() in self.all_letters:
				if not right and not letter in self.prev:
					self.attempt[0] += 1
				self.prev.append(letter)

		self.label_3.setText('Attempt left '+ str(7 - self.attempt[0]))
		self.label.setText(f'Description: {self.word["description"]}')
		self.label_2.setText(f"Word: {' '.join(self.answered)}")
		self.stickman_update()
		if 7 - self.attempt[0] <= 0:
			self.gameover()
		elif self.word['word']==''.join(self.answered):
			self.win()

	def gameover(self):
		QMessageBox.information(self,"Game Over", f"Right word is {self.word['word']}\nYou loose this game")
		self.close()

	def win(self):
		QMessageBox.information(self,"Win", f"Right word is {self.word['word']}\nСongratulations, you guessed this word)")
		self.close()

	def resizeEvent(self,event):
		self.resized.emit()
		return super(MainApp, self).resizeEvent(event)
	def on_mwresize(self):
		if self.geometry().height() < 642:
			self.verticalFrame_2.setHidden(True)
		elif self.geometry().height() >= 642:
			self.verticalFrame_2.setHidden(False)
	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()
		for x in range(0,len(self.all_letters)):
			if self.all_letters[x] == e.text().upper():
				eval(f'self.key_pressed(self.pushButton_{x+1})')
	def key_pressed(self, letter):
		if letter.text() != "":
			self.logic(letter.text())
			letter.setText("")
	def setListener(self):
		self.all_letters = []
		for x in range(1,27):
			eval(f'self.pushButton_{x}.clicked.connect(partial(self.key_pressed,self.pushButton_{x}))')
			eval(f"self.all_letters.append(self.pushButton_{x}.text())")

if __name__ == "__main__":

	app = QApplication(sys.argv)
	ex = MainApp()
	sys.exit(app.exec_())
