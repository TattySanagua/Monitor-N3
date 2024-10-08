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
        data = Query.get_embalse_freatimetros()

        if data.empty:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            column_names = ["Fecha", "Nivel de embalse [msnm]"]
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            return

        column_names = ["Fecha", "Nivel de embalse [msnm]"]
        freatimetro_columns = []

        for i, row in data.iterrows():
            freatimetros_concatenados = row['nivel_freatico']

            if not freatimetros_concatenados:
                continue

            freatimetros = freatimetros_concatenados.split('; ')

            for freatimetro in freatimetros:
                if ': ' in freatimetro:
                    nombre_freatimetro, _ = freatimetro.split(': ')
                else:
                    # Si no hay valor asociado, solo se tiene el nombre
                    nombre_freatimetro = freatimetro

                # Añadir el nombre del freatímetro a las columnas si no está ya
                if nombre_freatimetro not in freatimetro_columns:
                    freatimetro_columns.append(nombre_freatimetro)

        column_names.extend(freatimetro_columns)

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for i, row in data.iterrows():
            fecha = row['fecha']
            nivel_embalse = row['nivel_embalse']
            formatted_date = fecha.strftime("%d/%m/%Y")
            self.tableWidget.setItem(i, 0, QTableWidgetItem(formatted_date))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(nivel_embalse)))

            freatimetros_concatenados = row['nivel_freatico']

            if freatimetros_concatenados:
                freatimetros = freatimetros_concatenados.split('; ')

                # Crear un diccionario para almacenar los valores de cada freatímetro
                freatimetro_dict = {}

                for freatimetro in freatimetros:
                    if ': ' in freatimetro:
                        nombre_freatimetro, valor = freatimetro.split(': ')
                    else:
                        nombre_freatimetro = freatimetro
                        valor = '-'
                    freatimetro_dict[nombre_freatimetro] = valor

                # Llenar la tabla con los valores correspondientes
                for j, freatimetro_name in enumerate(freatimetro_columns, start=2):
                    valor = freatimetro_dict.get(freatimetro_name, '-')
                    self.tableWidget.setItem(i, j, QTableWidgetItem(valor))

        self.tableWidget.resizeColumnsToContents()