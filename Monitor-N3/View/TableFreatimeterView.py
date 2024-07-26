from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QLabel, QGridLayout
from DataBase.Query import Query
import pandas as pd

class TablaFreatimetroView(QMainWindow):
    def __init__(self):
        super(TablaFreatimetroView,self).__init__()
        self.setWindowTitle("Tabla de Freatímetro")
        self.setGeometry(200, 100, 550, 700)
        self.create_layout()

    def create_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")

        layout = QGridLayout()
        central_widget.setLayout(layout)

        self.tableWidget = QTableWidget()
        layout.addWidget(lbl_v1, 0, 0, 1, 1)
        layout.addWidget(self.tableWidget, 0, 1, 1, 1)
        layout.addWidget(lbl_v2, 0, 2, 1, 1)
        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")
        footer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer_label, 2, 1, 1, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 0)

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