from PyQt5.QtCore import QObject, pyqtSignal

class DataUpdater(QObject):
    data_updated_signal = pyqtSignal()

    def __init__(self):
        super(DataUpdater, self).__init__()

    def update_data(self):
        self.data_updated_signal.emit()
