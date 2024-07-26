import math
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel
from DataBase.Query import Query

class FormInstrumentsView(QMainWindow):
    def __init__(self):
        super(FormInstrumentsView,self).__init__()
        self.setWindowTitle("Agregar Instrumento")
        self.setGeometry(200, 100, 850, 700)
        self.setup_ui()

    def setup_ui(self):
        lbl_titulo_ppal = QLabel("Próximamente..", self)