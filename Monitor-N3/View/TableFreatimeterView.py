from PyQt5.QtWidgets import QMainWindow,QTableWidget, QTableWidgetItem
from DataBase.Query import Query
import pandas as pd

class TablaFreatimetroView(QMainWindow):
    def __init__(self):
        super(TablaFreatimetroView,self).__init__()
        self.setWindowTitle("Tabla de Freatímetro")
        self.setGeometry(100, 100, 600, 700)
        self.create_table()

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50,50,400,600)
        self.update_table()

    def update_table(self):
        self.tableWidget.clear()
        data = Query.get_l3_f1()

        if data.empty:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Fecha", "Nivel de embalse [msnm]", "Nivel freático [msnm]"]

            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data.columns))

        column_names = ["Fecha", "Nivel de embalse [msnm]", "Nivel freático [msnm]"]

        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for i, row in data.iterrows():
            for j, item in enumerate(row):
                if pd.isnull(item):
                    item = '-'
                elif j == 0:
                    formatted_date = item.strftime("%d/%m/%Y")
                    self.tableWidget.setItem(i, j, QTableWidgetItem(formatted_date))
                    continue
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

        self.tableWidget.resizeColumnsToContents()