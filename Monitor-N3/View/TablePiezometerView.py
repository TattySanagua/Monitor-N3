import math

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QLabel, QGridLayout
from DataBase.Query import Query

class TablaPiezometrosView(QMainWindow):
    def __init__(self):
        super(TablaPiezometrosView,self).__init__()
        self.setWindowTitle("Tabla de Piezómetros")
        self.setGeometry(150, 100, 1200, 700)
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
        data = Query.get_embalse_piezometros()

        if data.empty:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Fecha", "Nivel de embalse [msnm]"]
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        column_names = ["Fecha", "Nivel de embalse [msnm]"]
        piezometro_columns = []

        for i, row in data.iterrows():
            piezometros_concatenados = row['nivel_piezometrico']

            if not piezometros_concatenados:
                continue

            piezometros = piezometros_concatenados.split('; ')

            for piezometro in piezometros:
                if ': ' in piezometro:
                    nombre_piezometro, _ = piezometro.split(': ')
                else:
                    nombre_piezometro = piezometro

                if nombre_piezometro not in piezometro_columns:
                    piezometro_columns.append(nombre_piezometro)

        column_names.extend(piezometro_columns)

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for i, row in data.iterrows():
            fecha = row['fecha']
            nivel_embalse = row['nivel_embalse']
            formatted_date = fecha.strftime("%d/%m/%Y")
            self.tableWidget.setItem(i, 0, QTableWidgetItem(formatted_date))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(nivel_embalse)))

            piezometros_concatenados = row['nivel_piezometrico']

            if piezometros_concatenados:
                piezometros = piezometros_concatenados.split('; ')

                piezometro_dict = {}

                for piezometro in piezometros:
                    if ': ' in piezometro:
                        nombre_piezometro, valor = piezometro.split(': ')
                    else:
                        nombre_piezometro = piezometro
                        valor = '-'
                    piezometro_dict[nombre_piezometro] = valor

                for j, piezometro_name in enumerate(piezometro_columns, start=2):
                    valor = piezometro_dict.get(piezometro_name, '-')
                    self.tableWidget.setItem(i, j, QTableWidgetItem(valor))

        self.tableWidget.resizeColumnsToContents()