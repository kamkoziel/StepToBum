import json
import os

class ConfigControl():
    def __init__(self):
        if os.path.isfile('data\\config.json'):
           with open('data/config.json') as f:
               self.config = json.load(f)

        else:
            default={}
            default['recorded_files_name'] = "patient"
            default['recorded_files_path'] = "data/Rec"
            default['recorded_format'] = "audio/wav"
            default['disorder_path'] = "data/sample.wav"
            default['disorder_autoplay_time'] = 10
            with open('data/config.json', 'w') as outfile:
                json.dump(default, outfile)

            self.config = default

    def read(self, data= None):
        for item in self.config:
            print(item + ': '+ self.config[item] )

    def save(self):
        with open('data/config.json', 'w') as outfile:
            json.dump(self.config, outfile)

        return True

    @staticmethod
    def get_recPath():
        cfg = ConfigControl()
        if 'recorded_files_path' in cfg.config:
            return cfg.config['recorded_files_path']
        else:
            return ''

    @staticmethod
    def get_recName():
        cfg = ConfigControl()
        if 'recorded_files_name' in cfg.config:
            return cfg.config['recorded_files_name']
        else:
            return ''

    @staticmethod
    def get_disorderPath():
        cfg = ConfigControl()
        if 'disorder_path' in cfg.config:
            return cfg.config['disorder_path']
        else:
            return ''

    @staticmethod
    def get_recFormat():
        cfg = ConfigControl()
        if 'recorded_format' in cfg.config:
            return cfg.config['recorded_format']
        else:
            return ''

    @staticmethod
    def get_disorder_autoPlayTime():
        cfg = ConfigControl()
        if 'disorder_autoplay_time' in cfg.config:
            return cfg.config['disorder_autoplay_time']
        else:
            return ''

