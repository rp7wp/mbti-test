
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton)
from instr import *

global_ne = 0
global_ni = 0
global_te = 0
global_ti = 0
global_fe = 0
global_fi = 0
global_se = 0
global_si = 0

class Question1(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.ne = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(ne1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_ne)
        self.yes1.clicked.connect(self.update_ne)
        self.idk.clicked.connect(self.update_ne)
        self.no1.clicked.connect(self.update_ne)
        self.no2.clicked.connect(self.update_ne)

    def update_ne(self):
        if self.yes2.isChecked():
            self.ne = 2
        elif self.yes1.isChecked():
            self.ne = 1
        elif self.idk.isChecked():
            self.ne = 0
        elif self.no1.isChecked():
            self.ne = -1
        elif self.no2.isChecked():
            self.ne = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_ne
        global_ne += self.ne
        self.q2 = Question2()
        self.q2.show()
        self.close()

class Question2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.si = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(si1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_si)
        self.yes1.clicked.connect(self.update_si)
        self.idk.clicked.connect(self.update_si)
        self.no1.clicked.connect(self.update_si)
        self.no2.clicked.connect(self.update_si)

    def update_si(self):
        if self.yes2.isChecked():
            self.si = 2
        elif self.yes1.isChecked():
            self.si = 1
        elif self.idk.isChecked():
            self.si = 0
        elif self.no1.isChecked():
            self.si = -1
        elif self.no2.isChecked():
            self.si = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_si
        global_si += self.si
        self.q3 = Question3()
        self.q3.show()
        self.close()

class Question3(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.ti = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(ti1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_ti)
        self.yes1.clicked.connect(self.update_ti)
        self.idk.clicked.connect(self.update_ti)
        self.no1.clicked.connect(self.update_ti)
        self.no2.clicked.connect(self.update_ti)

    def update_ti(self):
        if self.yes2.isChecked():
            self.ti = 2
        elif self.yes1.isChecked():
            self.ti = 1
        elif self.idk.isChecked():
            self.ti = 0
        elif self.no1.isChecked():
            self.ti = -1
        elif self.no2.isChecked():
            self.ti = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_ti
        global_ti += self.ti
        self.q4 = Question4()
        self.q4.show()
        self.close()

class Question4(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.fi = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(fi1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_fi)
        self.yes1.clicked.connect(self.update_fi)
        self.idk.clicked.connect(self.update_fi)
        self.no1.clicked.connect(self.update_fi)
        self.no2.clicked.connect(self.update_fi)

    def update_fi(self):
        if self.yes2.isChecked():
            self.fi = 2
        elif self.yes1.isChecked():
            self.fi = 1
        elif self.idk.isChecked():
            self.fi = 0
        elif self.no1.isChecked():
            self.fi = -1
        elif self.no2.isChecked():
            self.fi = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_fi
        global_fi += self.fi
        self.q5 = Question5()
        self.q5.show()
        self.close()

class Question5(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.ne = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(ne2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_ne)
        self.yes1.clicked.connect(self.update_ne)
        self.idk.clicked.connect(self.update_ne)
        self.no1.clicked.connect(self.update_ne)
        self.no2.clicked.connect(self.update_ne)

    def update_ne(self):
        if self.yes2.isChecked():
            self.ne = 2
        elif self.yes1.isChecked():
            self.ne = 1
        elif self.idk.isChecked():
            self.ne = 0
        elif self.no1.isChecked():
            self.ne = -1
        elif self.no2.isChecked():
            self.ne = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_ne
        global_ne += self.ne
        self.q6 = Question6()
        self.q6.show()
        self.close()

class Question6(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.ni = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(ni1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_ni)
        self.yes1.clicked.connect(self.update_ni)
        self.idk.clicked.connect(self.update_ni)
        self.no1.clicked.connect(self.update_ni)
        self.no2.clicked.connect(self.update_ni)

    def update_ni(self):
        if self.yes2.isChecked():
            self.ni = 2
        elif self.yes1.isChecked():
            self.ni = 1
        elif self.idk.isChecked():
            self.ni = 0
        elif self.no1.isChecked():
            self.ni = -1
        elif self.no2.isChecked():
            self.ni = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_ni
        global_ni += self.ni
        self.q7 = Question7()
        self.q7.show()
        self.close()

class Question7(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.te = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(te1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_te)
        self.yes1.clicked.connect(self.update_te)
        self.idk.clicked.connect(self.update_te)
        self.no1.clicked.connect(self.update_te)
        self.no2.clicked.connect(self.update_te)

    def update_te(self):
        if self.yes2.isChecked():
            self.te = 2
        elif self.yes1.isChecked():
            self.te = 1
        elif self.idk.isChecked():
            self.te = 0
        elif self.no1.isChecked():
            self.te = -1
        elif self.no2.isChecked():
            self.te = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_te
        global_te += self.te
        self.q8 = Question8()
        self.q8.show()
        self.close()

class Question8(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.ni = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(ni2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_ni)
        self.yes1.clicked.connect(self.update_ni)
        self.idk.clicked.connect(self.update_ni)
        self.no1.clicked.connect(self.update_ni)
        self.no2.clicked.connect(self.update_ni)

    def update_ni(self):
        if self.yes2.isChecked():
            self.ni = 2
        elif self.yes1.isChecked():
            self.ni = 1
        elif self.idk.isChecked():
            self.ni = 0
        elif self.no1.isChecked():
            self.ni = -1
        elif self.no2.isChecked():
            self.ni = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_ni
        global_ni += self.ni
        self.q9 = Question9()
        self.q9.show()
        self.close()

class Question9(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.se = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(se1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_se)
        self.yes1.clicked.connect(self.update_se)
        self.idk.clicked.connect(self.update_se)
        self.no1.clicked.connect(self.update_se)
        self.no2.clicked.connect(self.update_se)

    def update_se(self):
        if self.yes2.isChecked():
            self.se = 2
        elif self.yes1.isChecked():
            self.se = 1
        elif self.idk.isChecked():
            self.se = 0
        elif self.no1.isChecked():
            self.se = -1
        elif self.no2.isChecked():
            self.se = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_se
        global_se += self.se
        self.q10 = Question10()
        self.q10.show()
        self.close()

class Question10(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.fe = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(fe1)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_fe)
        self.yes1.clicked.connect(self.update_fe)
        self.idk.clicked.connect(self.update_fe)
        self.no1.clicked.connect(self.update_fe)
        self.no2.clicked.connect(self.update_fe)

    def update_fe(self):
        if self.yes2.isChecked():
            self.fe = 2
        elif self.yes1.isChecked():
            self.fe = 1
        elif self.idk.isChecked():
            self.fe = 0
        elif self.no1.isChecked():
            self.fe = -1
        elif self.no2.isChecked():
            self.fe = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_fe
        global_fe += self.fe
        self.q11 = Question11()
        self.q11.show()
        self.close()

class Question11(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.si = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(si2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_si)
        self.yes1.clicked.connect(self.update_si)
        self.idk.clicked.connect(self.update_si)
        self.no1.clicked.connect(self.update_si)
        self.no2.clicked.connect(self.update_si)

    def update_si(self):
        if self.yes2.isChecked():
            self.si = 2
        elif self.yes1.isChecked():
            self.si = 1
        elif self.idk.isChecked():
            self.si = 0
        elif self.no1.isChecked():
            self.si = -1
        elif self.no2.isChecked():
            self.si = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_si
        global_si += self.si
        self.q12 = Question12()
        self.q12.show()
        self.close()

class Question12(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.fe = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(fe2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def score(self):
        self.yes2.clicked.connect(self.update_fe)
        self.yes1.clicked.connect(self.update_fe)
        self.idk.clicked.connect(self.update_fe)
        self.no1.clicked.connect(self.update_fe)
        self.no2.clicked.connect(self.update_fe)

    def update_fe(self):
        if self.yes2.isChecked():
            self.fe = 2
        elif self.yes1.isChecked():
            self.fe = 1
        elif self.idk.isChecked():
            self.fe = 0
        elif self.no1.isChecked():
            self.fe = -1
        elif self.no2.isChecked():
            self.fe = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_fe
        global_fe += self.fe
        self.q13 = Question13()
        self.q13.show()
        self.close()

class Question13(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.fi = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(fi2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)
    

    def score(self):
        self.yes2.clicked.connect(self.update_fi)
        self.yes1.clicked.connect(self.update_fi)
        self.idk.clicked.connect(self.update_fi)
        self.no1.clicked.connect(self.update_fi)
        self.no2.clicked.connect(self.update_fi)

    def update_fi(self):
        if self.yes2.isChecked():
            self.fi = 2
        elif self.yes1.isChecked():
            self.fi = 1
        elif self.idk.isChecked():
            self.fi = 0
        elif self.no1.isChecked():
            self.fi = -1
        elif self.no2.isChecked():
            self.fi = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_fi
        global_fi += self.fi
        self.q14 = Question14()
        self.q14.show()
        self.close()

class Question14(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.te = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(te2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)


    def score(self):
        self.yes2.clicked.connect(self.update_te)
        self.yes1.clicked.connect(self.update_te)
        self.idk.clicked.connect(self.update_te)
        self.no1.clicked.connect(self.update_te)
        self.no2.clicked.connect(self.update_te)

    def update_te(self):
        if self.yes2.isChecked():
            self.te = 2
        elif self.yes1.isChecked():
            self.te = 1
        elif self.idk.isChecked():
            self.te = 0
        elif self.no1.isChecked():
            self.te = -1
        elif self.no2.isChecked():
            self.te = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_te
        global_te += self.te
        self.q15 = Question15()
        self.q15.show()
        self.close()

class Question15(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.ti = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(ti2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)


    def score(self):
        self.yes2.clicked.connect(self.update_ti)
        self.yes1.clicked.connect(self.update_ti)
        self.idk.clicked.connect(self.update_ti)
        self.no1.clicked.connect(self.update_ti)
        self.no2.clicked.connect(self.update_ti)

    def update_ti(self):
        if self.yes2.isChecked():
            self.ti = 2
        elif self.yes1.isChecked():
            self.ti = 1
        elif self.idk.isChecked():
            self.ti = 0
        elif self.no1.isChecked():
            self.ti = -1
        elif self.no2.isChecked():
            self.ti = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_ti
        global_ti += self.ti
        self.q16 = Question16()
        self.q16.show()
        self.close()

class Question16(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.score()
        self.connects()
        self.show()

        self.se = 0

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(se2)
        self.yes2 = QRadioButton(absolutely_yes)
        self.yes1 = QRadioButton(yes)
        self.idk = QRadioButton(idk)
        self.no1 = QRadioButton(no)
        self.no2 = QRadioButton(absolutely_no)
        self.next = QPushButton('следующий вопрос!（￣︶￣）↗　')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.yes1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.idk, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.no2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout)


    def score(self):
        self.yes2.clicked.connect(self.update_se)
        self.yes1.clicked.connect(self.update_se)
        self.idk.clicked.connect(self.update_se)
        self.no1.clicked.connect(self.update_se)
        self.no2.clicked.connect(self.update_se)

    def update_se(self):
        if self.yes2.isChecked():
            self.se = 2
        elif self.yes1.isChecked():
            self.se = 1
        elif self.idk.isChecked():
            self.se = 0
        elif self.no1.isChecked():
            self.se = -1
        elif self.no2.isChecked():
            self.se = -2

    def connects(self):
        self.next.clicked.connect(self.next_click)
    
    def next_click(self):
        global global_se
        global_se += self.se
        self.final_win = FinalWin()
        self.final_win.show()
        self.close()

