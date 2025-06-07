from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel)
from questions import *

data = {
    'si': si,
    'se': se,
    'ti': ti,
    'te': te,
    'fi': fi,
    'fe': fe,
    'ni': ni,
    'ne': ne
}

#проверка
def check_conditions(vars_list):
    #чередуются i/e
    for i in range(1, len(vars_list)):
        if vars_list[i][1] == vars_list[i - 1][1]:
            return False

    #s/t/f/n встречаются не раньше чем через 4 переменные
    for i in range(len(vars_list)):
        for j in range(i + 1, min(i + 5, len(vars_list))):
            if vars_list[i][0] == vars_list[j][0]:
                return False

    return True

#сортировка в порядке убывания
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)


from itertools import permutations

for perm in permutations(sorted_data):
    if check_conditions(perm):
        sorted_data = perm
        break

#признаюсь это ⬆️⬆️⬆️ через chatgpt писала, я не придумала как это оформить

class FinalWin(QWidget):
    def __init__(self):
            super().__init__()
            self.set_appear()
            self.initUI()
            self.show()

    def set_appear(self):
        self.setWindowTitle('mbti test by rp7wp 🐇')
        self.resize(500, 400)
        self.move(650, 300)

    def initUI(self):
        self.question1 = QLabel(sorted_data)

#не закончено!