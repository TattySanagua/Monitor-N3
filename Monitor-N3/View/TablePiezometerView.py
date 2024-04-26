import math

from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from DataBase.Query import Query

class TablaPiezometrosView(QMainWindow):
    def __init__(self):
        super(TablaPiezometrosView,self).__init__()
        self.setWindowTitle("Tabla de Piezómetros")
        self.setGeometry(100, 100, 1000, 700)
        self.create_table()

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 900, 600)
        self.update_table()

    def update_table(self):
        self.tableWidget.clear()
        data = Query.get_embalse_7piezometros()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        column_names = ["Fecha", "Nivel de embalse [msnm]", "Np PC1 [msnm]", "Np PC2 [msnm]", "Np PC3 [msnm]", "Np PC4 [msnm]", "Np PC5 [msnm]", "Np PC6 [msnm]", "Np PC7 [msnm]"]

        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                if item is None or (isinstance(item, float) and math.isnan(item)):
                    item = '-'
                elif j == 0:
                    formatted_date = item.strftime("%d/%m/%Y")
                    self.tableWidget.setItem(i, j, QTableWidgetItem(formatted_date))
                    continue
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

        self.tableWidget.resizeColumnsToContents()