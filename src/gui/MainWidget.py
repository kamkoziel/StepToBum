import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QSlider, QPushButton, QMainWindow
from PyQt5.QtWidgets import QWidget
from src.gui.RecordButton import RecordButton
from src.controls.MicrophoneRecorder import MicrophoneRecorder
from src.gui.AudioWavePlot import AudioWavePlot
from src.controls.config_control import ConfigControl
from src.gui.time_counter import TimeCounter


class MainWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.main_window: QMainWindow = parent
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 800
        self.leftPanelWidth = 250
        self.initUI()
        self.initMplWidget()
        self.sample = QSound(ConfigControl.get_disorderPath())

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.recordButton = RecordButton()
        self.recordButton.clicked.connect(self.on_recordButton)

        self.playDisorder = QPushButton('Play disorder')
        self.playDisorder.setDisabled(False)
        self.playDisorder.clicked.connect(self.playSample)

        self.lcd_time_counter = TimeCounter()
        self.wavePlot = AudioWavePlot(self)

        labelsLayout = QHBoxLayout()
        labelsLayout.addWidget(self.recordButton)
        labelsLayout.addWidget(self.playDisorder)
        labelsLayout.addWidget(self.lcd_time_counter)
        labelsLayout.setAlignment(Qt.AlignLeft)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(labelsLayout)
        mainLayout.addWidget(self.wavePlot.toolbar)
        mainLayout.addWidget(self.wavePlot.canvas)

    def on_recordButton(self):
        if self.recordButton.isChecked():
            self.initData()
            self.initTimer()
            self.recordButton.setStyleSheet(self.recordButton.record_stylesheet)
            self.recordButton.setText('Recording ...')
            self.timer.timeout.connect(self.handleNewData)
            self.lcd_time_counter.start()
            self.main_window.statusBar().showMessage('Recording...')
            print(int(ConfigControl.get_disorder_autoPlayTime()))

            if self.main_window.menu_bar.autoPlay.isChecked():
                self.timer.singleShot(int(ConfigControl.get_disorder_autoPlayTime()) * 1000,self.playSample)

            self.timer.start(50)
        else:
            self.recordButton.setStyleSheet(self.recordButton.stop_stylesheet)
            self.recordButton.setText('Rec')
            self.main_window.statusBar().showMessage('Recording finish')
            self.lcd_time_counter.stop()
            self.main_window.statusBar().showMessage('Saving file')
            self.mic.write_to_wav(10)
            self.timer.stop()
            self.sample.stop()
            del self.mic
            self.main_window.statusBar().showMessage('Recording finish')


    def initMplWidget(self):
        """creates initial matplotlib plots in the main window and keeps
        references for further use"""
        # top plot
        self.time_vect_primary = np.arange(1024, dtype=np.float32) / 4000 * 1000
        self.ax_top = self.wavePlot.figure.add_subplot(111)
        self.ax_top.set_ylim(-32768, 32768)
        self.ax_top.set_xlim(0, self.time_vect_primary.max())
        self.ax_top.set_xlabel(u'time (ms)', fontsize=6)

        # line objects
        self.line_top, = self.ax_top.plot(self.time_vect_primary, np.ones_like(self.time_vect_primary))

    def handleNewData(self):
        """ handles the asynchroneously collected sound chunks """
        # gets the latest frames
        frames = self.mic.get_frames()

        if len(frames) > 0:
            # keeps only the last frame
            current_frame = frames[-1]

            # plots the time signal
            self.line_top.set_data(self.time_vect_primary, current_frame)

            # refreshes the plots
            self.wavePlot.canvas.draw()

    def initData(self):
        mic = MicrophoneRecorder()
        mic.start()
        self.mic = mic
        # computes the parameters that will be used during plotting
        self.time_vect_primary = np.arange(mic.chunksize, dtype=np.float32) / mic.rate * 1000

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleNewData)

    def playSample(self):
        self.sample.play()


