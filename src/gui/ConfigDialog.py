from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QLineEdit, QLabel, QPushButton, QHBoxLayout, \
    QGroupBox, QComboBox
from src.controls.audio_support_settings import AudioSupport
from src.controls.config_control import ConfigControl

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)

        self.setModal(True)
        self.setWindowTitle('SETTINGS')
        self.setStyleSheet(self.__getStyle())

        self.initUI()

    def initUI(self):
        labelPath = QLabel('Recorded files directory:')
        labelFormat = QLabel('Audio format: ')
        labelName = QLabel('Audio files names:')

        self.recName = QLineEdit()
        self.recName.setText(ConfigControl.get_recName())

        self.recPath = QLineEdit()
        self.recPath.setText(ConfigControl.get_recPath())
        self.getPathBtn = QPushButton('...')
        self.getPathBtn.setMaximumWidth(30)
        pathItemsLayout = QHBoxLayout()
        pathItemsLayout.addWidget(self.recPath)
        pathItemsLayout.addWidget(self.getPathBtn)

        self.filesFormat = QComboBox()
        self._fillFormats()
        self.filesFormat.setDisabled(True)

        audioGLayout = QVBoxLayout()
        audioGLayout.setAlignment(Qt.AlignTop)
        audioGLayout.addWidget(labelName)
        audioGLayout.addWidget(self.recName)
        audioGLayout.addWidget(labelPath)
        audioGLayout.addLayout(pathItemsLayout)
        audioGLayout.addWidget(labelFormat)
        audioGLayout.addWidget(self.filesFormat)

        recAudioGroup = QGroupBox('Recording audio settings')
        recAudioGroup.setLayout(audioGLayout)

        labelPath2 = QLabel('Path to disorder file:')
        self.disordePath = QLineEdit()
        self.disordePath.setText(ConfigControl.get_disorderPath())

        labelDisorderTime = QLabel('Autoplay time in seconds:')
        self.disorderAutoplayTime = QLineEdit()

        self.disorderAutoplayTime.setText(ConfigControl.get_disorder_autoPlayTime())

        playAudioLayout = QVBoxLayout()
        playAudioLayout.addWidget(labelPath2)
        playAudioLayout.addWidget(self.disordePath)
        playAudioLayout.addWidget(labelDisorderTime)
        playAudioLayout.addWidget(self.disorderAutoplayTime)

        playAudioGroup = QGroupBox('Played audio settings')
        playAudioGroup.setLayout(playAudioLayout)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(recAudioGroup)
        layout.addWidget(playAudioGroup)
        layout.addWidget(self.buttons)

    def showDialog(self, parent=None):
        dialog = ConfigDialog(parent)
        is_save = dialog.exec()

        if is_save:
            config = ConfigControl()
            config.config["recorded_files_name"] = dialog.recName.text()
            config.config["recorded_format"] = dialog.filesFormat.itemText(dialog.filesFormat.currentIndex())
            config.config["disorder_path"] = dialog.disordePath.text()
            config.config["disorder_autoplay_time"] = dialog.disorderAutoplayTime.text()
            config.save()
            del config

            print('Configuration done')
            return True
        else:
            return False

    def _fillFormats(self):
       audioType = AudioSupport()
       for item in audioType.containers:
           self.filesFormat.addItem(str(item))

    def __getStyle(self):
        css_file = open('data\\dialog_style.css','r')
        style = css_file.read()

        return style