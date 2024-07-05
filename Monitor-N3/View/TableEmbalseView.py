import math
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from DataBase.Query import Query

class TablaEmbalseView(QMainWindow):
    def __init__(self):
        super(TablaEmbalseView,self).__init__()
        self.setWindowTitle("Tabla de Embasle y Precipitaciones")
        self.setGeometry(150, 100, 1100, 700)
        self.create_table()

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 1000, 600)
        self.update_table()

    def update_table(self):
        self.tableWidget.clear()
        data = Query.get_precipiaciones()

        if not data:  # Verificar si data está vacío
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Fecha", "Nivel de embalse [msnm]", "Precipitación [mm]", "Precip 3 días previos [mm]",
                            "Precip. 5 días previos [mm]", "Precip. 10 días previos [mm]"]
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        column_names = ["Fecha", "Nivel de embalse [msnm]", "Precipitación [mm]", "Precip 3 días previos [mm]", "Precip. 5 días previos [mm]", "Precip. 10 días previos [mm]"]

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