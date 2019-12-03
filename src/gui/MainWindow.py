from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.gui.MainWidget import MainWidget

from src.gui.MenuBar import MenuBarWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 40
        self.top = 80
        self.width = 800
        self.height = 600
        self.title = 'POMwJO Project - Blood elements counter'
        self.styles = open('data\\style.css','r')

        self.initUI()

    def initUI(self):
        self.main_widget = MainWidget(self)
        self.menu_bar = MenuBarWidget(self.main_widget)
        self.setStyleSheet(self.getStyle())
        self.setWindowIcon(QtGui.QIcon('img/DPC.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMenuBar(self.menu_bar)
        self.statusBar().showMessage('Ready')
        self.setCentralWidget(self.main_widget)

        self.show()

    def getStyle(self):
        css_file = open('data\\style.css','r')
        style = css_file.read()

        return style

