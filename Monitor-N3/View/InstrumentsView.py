import math

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QWidget, QGridLayout, QPushButton
from DataBase.Query import Query

class InstrumentsView(QMainWindow):
    def __init__(self):
        super(InstrumentsView,self).__init__()
        self.setWindowTitle("Instrumentos")
        self.setGeometry(200, 100, 850, 700)
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
        data = Query.get_instrumentos()

        if data.empty:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Nombre", "Tipo", "Medición", "Fecha de instalación", "Fecha de baja", "Activo", "Dar de baja"]
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data.columns) + 1)

        column_names = ["Nombre", "Tipo", "Medición", "Fecha de instalación", "Fecha de baja", "Activo", "Dar de baja"]

        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for i, row in data.iterrows():
            for j, item in enumerate(row):
                if j == 5:
                    item = "SI" if item == 1 else "NO"
                if pd.isnull(item):
                    item = '-'
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

            btn_baja = QPushButton("X")
            btn_baja.clicked.connect(lambda _, row_index=i: self.dar_de_baja(row_index))
            self.tableWidget.setCellWidget(i, len(row), btn_baja)

        self.tableWidget.resizeColumnsToContents()

    def dar_de_baja(self, row_index):
        nombre_instrumento = self.tableWidget.item(row_index,0).text()
        Query.delete_instrument(nombre_instrumento)
        self.update_table()