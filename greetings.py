from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout)
from instr import *
from questions import Question1

class FirstWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.hello = QLabel(mhello)
        self.desc1 = QLabel(mdesc1)
        self.desc2 = QLabel(mdesc2)
        self.desc3 = QLabel(mdesc3)
        self.glhf = QLabel(mglhf)
        self.start = QPushButton(mstart)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.desc1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.desc2, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.desc3, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.glhf, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.start, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.start.clicked.connect(self.next_click)

    def next_click(self):
        self.q1 = Question1()
        self.q1.show()
        self.close()

app = QApplication([])
first_win = FirstWin()
first_win.show()
app.exec_()