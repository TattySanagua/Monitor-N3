import math
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel
from DataBase.Query import Query

class InstrumentsView(QMainWindow):
    def __init__(self):
        super(InstrumentsView,self).__init__()
        self.setWindowTitle("Instrumentos")
        self.setGeometry(200, 100, 850, 700)
        self.create_table()

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 750, 600)
        lbl_titulo_ppal = QLabel("Próximamente..", self)
        #self.update_table()