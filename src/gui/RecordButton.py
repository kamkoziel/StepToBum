from PyQt5.QtWidgets import QPushButton

class RecordButton(QPushButton):

    def __init__(self):
        super().__init__('Rec')
        self.stop_stylesheet = 'background: red; color: white;  min-width: 40px; max-width: 100px;'
        self.record_stylesheet = 'background: FireBrick; color: white;  min-width: 40px; max-width: 100px;'
        self.setStyleSheet(self.stop_stylesheet)
        self.setCheckable(True)
        self.setChecked(False)
