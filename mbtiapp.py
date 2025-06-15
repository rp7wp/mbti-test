
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QButtonGroup)
from instr import *
from itertools import chain, product
from random import shuffle


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
        self.q = QuestionsWidget()
        self.q.show()
        self.close()











questions = {
    'Ti': [
        'мне кажется, что понимание принципов важнее запоминания фактов',
        'меня не волнует, если мои рассуждения не понимают, когда я сам уверен в их правильности.'
    ],
    'Te': [
        'я принимаю решения, руководствуясь логикой и фактами, а не чувствами',
        'я быстро замечаю недостатки в работе других.'
    ],
    'Fi': [
        'я обладаю слепой моралью и могу полностью изменить свое мнение о человеке по одному его поступку',
        'я не могу делать то, что считаю неправильным, даже под давлением.'
    ],
    'Fe': [
        'я легко чувствую эмоции и переживания других людей.',
        'мне важно, чтобы окружающие одобряли мои слова и поступки.',
    ],
    'Ni': [
        'меня часто посещают различные предчувствия: я чувствую, что действия будут иметь определенные последствия',
        'я стараюсь найти скрытый смысл даже в поверхностных вещах.'
    ],
    'Ne': [
        'мои мысли быстро переключаются с одной темы на другую.',
        'мне нравится обсуждать нестандартные теории и сценарии.'
    ],
    'Si': [
        'я хорошо помню детали прошлых событий и могу их воспроизвести.',
        'я предпочитаю действовать только по проверенными мной путям, чтобы избежать неудач.'
    ],
    'Se': [
        'я быстро приспосабливаюсь к новым обстоятельствам и окружению.',
        'я наслаждаюсь моментом и мало задумываюсь о будущем.',
    ],
}

def question():
    all = list( # прривести всё к списку,
        chain( # ообъединить много последоовательностей в одну
               # chain("ABC", "DEF") => "ABCDEF"
            *(# * переводит список аргументов в перечисление chain(*[A,B]) => chain(A, B)
                product([c], questions[c]) # {'A': { 'B', 'C" } => [('A', "B"), ('A", 'C')]
                    for c # всех категорий (Ni, ,Ne ...)
                        in questions.keys() # возввращает список ключей в словаре
            )))
    shuffle(all) # перемешать
    yield from all # возвращать по одному, делаем генератор
    yield None

class QuestionsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.initializePage()

    def initializePage(self):
        self.complete = False
        self.answers = {
            'Ti': 0,
            'Te': 0,
            'Fi': 0,
            'Fe': 0,
            'Ni': 0,
            'Ne': 0,
            'Si': 0,
            'Se': 0,
        }
        self.question = question()
        self.current_question = next(self.question)
        self.sentense.setText(self.current_question[1])

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):

        self.gb = QGroupBox(self)
        self.no2 = QRadioButton(self.gb)
        self.no1 = QRadioButton(self.gb)
        self.idontknow = QRadioButton(self.gb)
        self.yes1 = QRadioButton(self.gb)
        self.yes2 = QRadioButton(self.gb) #группа кнопок с ответами

        self.no2.setText(absolutely_no)
        self.no1.setText(no)
        self.idontknow.setText(idk)
        self.yes1.setText(yes)
        self.yes2.setText(absolutely_yes) #текст у кнопок

        self.buttons = QButtonGroup(self.gb)
        self.buttons.setExclusive(True)
        self.buttons.addButton(self.no2)
        self.buttons.addButton(self.no1)
        self.buttons.addButton(self.idontknow)
        self.buttons.addButton(self.yes1)
        self.buttons.addButton(self.yes2) #добавить кнопки в группу

        # id == Баллы за ответ + 2
        self.buttons.setId(self.no2, 0)
        self.buttons.setId(self.no1, 1)
        self.buttons.setId(self.idontknow, 2)
        self.buttons.setId(self.yes1, 3)
        self.buttons.setId(self.yes2, 4)

        self.layout = QVBoxLayout(self.gb)
        self.layout.addWidget(self.no2)
        self.layout.addWidget(self.no1)
        self.layout.addWidget(self.idontknow)
        self.layout.addWidget(self.yes1)
        self.layout.addWidget(self.yes2)
        self.layout2 = QVBoxLayout(self)
        self.sentense = QLabel(self)
        self.sentense.setWordWrap(True)
        self.agree = QPushButton("выбор сделан")
        self.agree.setEnabled(False)
        self.layout2.addWidget(self.sentense)
        self.layout2.addWidget(self.gb, 1)
        self.layout2.addWidget(self.agree)

        self.buttons.idClicked.connect(lambda: self.agree.setEnabled(True))
        self.agree.clicked.connect(self.next_sentence)

    def next_sentence(self):
        self.answers[self.current_question[0]] += self.buttons.checkedId() - 2
        self.current_question = next(self.question)
        if self.current_question is None:
            self.resultss = ResultPage()
            self.resultss.show()
            self.close()
        else:
            self.sentense.setText(self.current_question[1])
            self.no2.setChecked(False)
            self.no1.setChecked(False)
            self.idontknow.setChecked(False)
            self.yes1.setChecked(False)
            self.yes2.setChecked(False)
            self.agree.setEnabled(False)

    def isComplete(self):
        return self.complete

class ResultPage(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.layout = QVBoxLayout()
        self.text = QLabel('''               Результаты:

                                                🏗️🚧👷
            ---------------------------------------------------------------------------------------
             Эта страница пока не завершена, просим прощения за неудобства!''')
        self.layout.addWidget(self.text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)


app = QApplication([])
first_win = FirstWin()
first_win.show()
app.exec_()
