from time import strftime
from PyQt5.QtWidgets import QWidget, QLCDNumber, QHBoxLayout
from PyQt5.QtCore import QTimer


class TimeCounter(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.countTime)
        self.initUI()

    def initUI(self):

        self.minutes = 0
        self.miliseconds = 0
        self.seconds = 0
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(12)
        self.lcd.display(str(self.minutes) + ' : ' + str(self.seconds) + ' : ' + str(self.miliseconds))

        layout = QHBoxLayout(self)
        layout.addWidget(self.lcd)


    def countTime(self):
        self.miliseconds = self.miliseconds + 1

        if self.miliseconds >= 100:
            self.miliseconds = 0
            self.seconds = self.seconds + 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes = self.minutes + 1

        self.lcd.display("{0}".format(str(self.minutes)) + ' : ' + str(self.seconds) + ' : ' + str(self.miliseconds))

    def start(self):

        if self.miliseconds != 0:
            self.miliseconds = 0
        if self.seconds != 0:
            self.seconds = 0
        if self.minutes != 0:
            self.minutes = 0
        self.timer.start(10)

    def stop(self):
        self.timer.stop()