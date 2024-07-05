import math
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from DataBase.Query import Query

class TablaAforadoresView(QMainWindow):
    def __init__(self):
        super(TablaAforadoresView,self).__init__()
        self.setWindowTitle("Tabla de Aforadores")
        self.setGeometry(200, 100, 850, 700)
        self.create_table()

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 750, 600)
        self.update_table()

    def update_table(self):
        self.tableWidget.clear()
        data = Query.get_embalse_aforadores()

        if not data:  # Verificar si data está vacío
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Fecha", "Nivel de embalse [msnm]", "Caudal AFo3-EI [l/s]", "Caudal AFo3-PP [l/s]",
                            "Caudal AFo3-TOT [l/s]", "Caudal Parshall[m3/s]"]

            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        column_names = ["Fecha", "Nivel de embalse [msnm]", "Caudal AFo3-EI [l/s]", "Caudal AFo3-PP [l/s]", "Caudal AFo3-TOT [l/s]", "Caudal Parshall[m3/s]"]

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