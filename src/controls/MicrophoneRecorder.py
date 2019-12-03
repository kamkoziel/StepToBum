import os
import wave
import pyaudio
import threading
import atexit
import numpy as np
from src.controls.config_control import ConfigControl


class MicrophoneRecorder(object):
    def __init__(self, rate=4000, chunksize=1024):
        self.rate = rate
        self.chunksize = chunksize
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunksize,
                                  stream_callback=self.new_frame)
        self.lock = threading.Lock()
        self.stop = False
        self.frames = []
        self.data =[]
        atexit.register(self.close)

    def new_frame(self, data, frame_count, time_info, status):
        data = np.fromstring(data, 'int16')
        with self.lock:
            self.frames.append(data)
            self.data.append(data)
            if self.stop:
                return None, pyaudio.paComplete
        return None, pyaudio.paContinue

    def get_frames(self):
        with self.lock:
            frames = self.frames
            self.frames = []
            return frames

    def get_data(self):
        return self.data

    def start(self):
        self.stream.start_stream()

    def close(self):
        with self.lock:
            self.stop = True
        self.stream.close()
        self.p.terminate()

    def write_to_wav(self,time):
        wf = wave.open(self.prep_recName(time), 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.get_data()))
        wf.close()

    def prep_recName(self,time ):
        fullname = ConfigControl.get_recPath()
        name = ConfigControl.get_recName()
        i = 0
        if not os.path.exists(fullname):
            os.mkdir(fullname)
        while os.path.exists(fullname+'/'+name+ str(i)+'.wav'):
            i += 1
        fullname = fullname+'/'+name+ str(i)+'.wav'
        return fullname