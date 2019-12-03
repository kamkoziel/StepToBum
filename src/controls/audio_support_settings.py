from PyQt5.QtMultimedia import QAudioRecorder


class AudioSupport():
    def __init__(self):
        r = QAudioRecorder()
        self.inputs = r.audioInputs()
        self.codecs = r.supportedAudioCodecs()
        self.rates = r.supportedAudioSampleRates()
        self.containers = r.supportedContainers()