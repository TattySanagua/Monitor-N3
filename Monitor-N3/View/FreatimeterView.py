from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QDateEdit, \
    QComboBox, QGridLayout
from mysql.connector import IntegrityError
from DataBase.Query import Query
from Signals.DataUpdater import DataUpdater
import Calculadora


class FreatimeterView(QWidget):

    def __init__(self, tabla_freatimetro_view):
        super(FreatimeterView, self).__init__()
        self.setup_ui()
        self.tabla_freatimetro_view = tabla_freatimetro_view
        self.data_updater = DataUpdater()
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

        # Diccionario de mapeo para insert
        self.insert_functions = {
            "L3-F1": Query.insert_data_l3_f1
        }

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("FREATÍMETRO", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha", self)
        lbl_v1 = QLabel("")

        self.lbl_freatimetro = QLabel("Freatímetro: ", self)

        self.cmbx_freatimetro = QComboBox(self)
        self.cmbx_freatimetro.setFixedWidth(150)
        self.cmbx_freatimetro.addItems(["L3-F1"])
        self.cmbx_freatimetro.currentIndexChanged.connect(self.actualizar_freatimetro)

        self.lbl_Nf = QLabel("Nivel freático = ")
        self.lbl_resultado = QLabel("")
        self.lbl_resultado.setFixedWidth(150)
        self.lbl_msnm = QLabel("msnm")

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(150)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lbl_lectura = QLabel("Lectura: ")
        self.lned_lectura_f = QLineEdit(self)
        self.lned_lectura_f.setFixedWidth(150)

        self.btn_calcular_nf = QPushButton("Calcular", self)
        self.btn_calcular_nf.setObjectName("btn")

        self.btn_guardar_nf = QPushButton("Guardar", self)
        self.btn_guardar_nf.setObjectName("btn")

        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)
        grid_layout.setRowStretch(2, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(5, 1)
        grid_layout.setRowStretch(7, 1)
        grid_layout.setRowStretch(9, 1)
        grid_layout.setRowStretch(11, 1)
        grid_layout.setRowStretch(13, 1)
        grid_layout.setRowStretch(15, 1)
        grid_layout.setRowStretch(16, 1)
        grid_layout.setRowStretch(17, 1)


        grid_layout.addWidget(lbl_titulo_ppal, 4, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 6, 0)
        grid_layout.addWidget(lbl_fecha, 6, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.date_edit, 6, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_freatimetro, 8, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmbx_freatimetro, 8, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_lectura, 10, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_lectura_f, 10, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_Nf, 12, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado, 12, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_msnm, 12, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_calcular_nf, 14, 1, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_guardar_nf, 14, 2, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 18, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.data_updater = DataUpdater()

        self.btn_calcular_nf.clicked.connect(self.calcular_nf)
        self.btn_guardar_nf.clicked.connect(self.guardar_nf)
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

    def calcular_nf(self):
        cb_values = [599.07]
        freatimetro_index = self.cmbx_freatimetro.currentIndex()
        cb = cb_values[freatimetro_index]

        lectura = self.lned_lectura_f.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, complete el campo numérico.")
            return
        else:
            try:
                lectura = float(lectura)
                resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
                self.lbl_resultado.setText(f"{resultado:.{decimales}f}")
                self.lned_lectura_f.clear()
            except ValueError:
                QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def guardar_nf(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        resultado = self.lbl_resultado.text()
        freatimetro = self.cmbx_freatimetro.currentText()

        if not fecha:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha.")
            return

        if not resultado:
            respuesta = QMessageBox.question(self, "Advertencia",
                                             "¿Está seguro que desea guardar el nivel freático en nulo?",
                                             QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.No:
                return

        try:
            if resultado:
                resultado = float(resultado)
            else:
                resultado = "NULL"

            insert_function = self.insert_functions[freatimetro]
            insert_function(fecha, resultado)
            self.lbl_resultado.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
            self.data_updater.update_data()
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error",
                                 "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def actualizar_freatimetro(self):
        self.lbl_lectura.clear()
        self.lbl_resultado.clear()

    def actualizar_tabla(self):
        self.tabla_freatimetro_view.update_table()