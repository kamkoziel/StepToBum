from PyQt5.QtCore import QFile, qWarning, QTimer, QIODevice, Qt
from PyQt5.QtWidgets import QMenuBar,  QAction, QMenu
from PyQt5.QtMultimedia import QSound
from src.gui.MainWidget import MainWidget
from src.gui.ConfigDialog import ConfigDialog
from src.controls.config_control import ConfigControl


class MenuBarWidget(QMenuBar):
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget: MainWidget = mainWidget

        self.file = self.addMenu("File")
        self.audio = self.addMenu("Audio")

        self.configDialog = QAction('Settings',self)
        self.configDialog.triggered.connect(ConfigDialog.showDialog)

        self.autoPlay = QAction('Autoplay disorder')
        self.autoPlay.setCheckable(True)
        self.autoPlay.setChecked(False)
        self.autoPlay.triggered.connect(self.changeBtn)

        self.playAudio = QAction('Play disorder')
        self.playAudio.triggered.connect(self.playSample)


        self.file.addAction(self.configDialog)
        self.audio.addAction(self.autoPlay)
        self.audio.addAction(self.playAudio)

    def playSample(self):
        QSound.play(ConfigControl.get_disorderPath())

    def changeBtn(self):
        if self.autoPlay.isChecked():
            self.mainWidget.playDisorder.setDisabled(1)
        else:
            self.mainWidget.playDisorder.setEnabled(1)

