import math

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QWidget, QVBoxLayout, QGridLayout
from DataBase.Query import Query

class TablaAforadoresView(QMainWindow):
    def __init__(self):
        super(TablaAforadoresView,self).__init__()
        self.setWindowTitle("Tabla de Aforadores")
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
        data = Query.get_embalse_aforadores()

        if data.empty:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Fecha", "Nivel de embalse [msnm]"]
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        column_names = ["Fecha", "Nivel de embalse [msnm]"]
        aforadores_columns = []

        for i, row in data.iterrows():
            aforadores_concatenados = row['caudal']

            if not aforadores_concatenados:
                continue

            aforadores = aforadores_concatenados.split('; ')

            for aforador in aforadores:
                if ': ' in aforador:
                    nombre_aforador, _ = aforador.split(': ')
                else:
                    nombre_aforador = aforador

                if nombre_aforador not in aforadores_columns:
                    aforadores_columns.append(nombre_aforador)

        column_names.extend(aforadores_columns)

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for i, row in data.iterrows():
            fecha = row['fecha']
            nivel_embalse = row['nivel_embalse']
            formatted_date = fecha.strftime("%d/%m/%Y")
            self.tableWidget.setItem(i, 0, QTableWidgetItem(formatted_date))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(nivel_embalse)))

            aforadores_concatenados = row['caudal']

            if aforadores_concatenados:
                aforadores = aforadores_concatenados.split('; ')

                aforador_dict = {}

                for aforador in aforadores:
                    if ': ' in aforador:
                        nombre_aforador, valor = aforador.split(': ')
                    else:
                        nombre_aforador = aforador
                        valor = '-'
                    aforador_dict[nombre_aforador] = valor

                for j, aforador_name in enumerate(aforadores_columns, start=2):
                    valor = aforador_dict.get(aforador_name, '-')
                    self.tableWidget.setItem(i, j, QTableWidgetItem(valor))

        self.tableWidget.resizeColumnsToContents()