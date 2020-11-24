import sys
from math import sqrt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Window(QMainWindow):
    def __init__(self):
        self.ch = ''
        self.prch = '0'
        self.d = ''
        self.flag = True
        self.er = 'Error'
        self.pointed = False
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(lambda: self.wr('1'))
        self.pushButton_2.clicked.connect(lambda: self.wr('2'))
        self.pushButton_3.clicked.connect(lambda: self.wr('3'))
        self.pushButton_5.clicked.connect(lambda: self.wr('4'))
        self.pushButton_6.clicked.connect(lambda: self.wr('5'))
        self.pushButton_7.clicked.connect(lambda: self.wr('6'))
        self.pushButton_9.clicked.connect(lambda: self.wr('7'))
        self.pushButton_10.clicked.connect(lambda: self.wr('8'))
        self.pushButton_11.clicked.connect(lambda: self.wr('9'))
        self.pushButton_14.clicked.connect(lambda: self.wr('0'))
        self.pushButton_13.clicked.connect(lambda: self.wr('.'))

        self.pushButton_20.clicked.connect(lambda: self.clean(1))
        self.pushButton_19.clicked.connect(lambda: self.clean(2))

        self.pushButton_4.clicked.connect(lambda: self.dey('+'))
        self.pushButton_8.clicked.connect(lambda: self.dey('-'))
        self.pushButton_12.clicked.connect(lambda: self.dey('*'))
        self.pushButton_15.clicked.connect(lambda: self.dey('^'))
        self.pushButton_16.clicked.connect(lambda: self.dey('/'))
        self.pushButton_17.clicked.connect(lambda: self.dey('sqr'))
        self.pushButton_18.clicked.connect(lambda: self.dey('='))

    def wr(self, op):
        if self.ch == 'Error':
            self.clean(1)
            self.wr(op)
        elif self.pointed and op == '.':
            self.ch = 'Error'
        elif op == '.' and (self.ch == '' or self.ch == '0'):
            self.pointed = True
            self.ch = '0.'
        elif op == '.':
            self.pointed = True
            self.ch += op
        elif self.ch == '0':
            self.ch = op
        else:
            self.ch += op
        self.label.setText(self.ch)

    def dey(self, per):
        if per != '=' and self.flag:
            self.d = per
            self.prch = self.ch
        if per != '=':
            self.d = per
        else:
            if self.d == '+':
                self.ch = str(float(self.prch) + float(self.ch))
            elif self.d == '-':
                self.ch = str(float(self.prch) - float(self.ch))
            elif self.d == '*':
                self.ch = str(float(self.prch) * float(self.ch))
            elif self.d == '/':
                self.ch = str(float(self.prch) / float(self.ch))
            elif self.d == '^':
                self.ch = str(float(self.prch) ** float(self.ch))
            elif self.d == 'sqr':
                if float(self.prch) > 0:
                    self.ch = str(sqrt(float(self.prch)))
                else:
                    self.ch = 'Error'
            if self.ch[-2:] == '.0':
                self.ch = self.ch[:-2]
            self.label.setText(self.ch)
            self.prch = self.ch
        self.ch = '0'
        self.flag = False

    def clean(self, w):
        if w == 1:
            self.ch = '0'
            self.prch = '0'
            self.d = ''
            self.flag = True
            self.pointed = False
            self.label.setText(self.ch)
        else:
            if len(self.ch) == 1:
                self.ch = '0'
                self.prch = '0'
                self.d = ''
            elif self.ch[-1] == '.':
                self.pointed = False
            self.ch = self.ch[:-1]
        self.label.setText(self.ch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())