from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QDateEdit, QComboBox
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

        lbl_titulo_ppal = QLabel("FREATÍMETROS", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(110)

        self.lbl_freatimetro = QLabel("Freatímetro: ", self)
        self.lbl_freatimetro.setFixedWidth(60)

        self.cmbx_freatimetro = QComboBox(self)
        self.cmbx_freatimetro.addItems(["L3-F1"])
        self.cmbx_freatimetro.currentIndexChanged.connect(self.actualizar_freatimetro)

        self.lbl_Nf = QLabel("Nf = ")
        self.lbl_Nf.setFixedWidth(60)
        self.lbl_resultado = QLabel("")
        self.lbl_resultado.setFixedWidth(100)
        self.lbl_msnm = QLabel("msnm")
        self.lbl_msnm.setFixedWidth(55)

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lbl_lectura = QLabel("Lectura: ")
        self.lbl_lectura.setFixedWidth(60)
        self.lned_lectura_f = QLineEdit(self)
        self.lned_lectura_f.setFixedWidth(160)

        self.btn_calcular_nf = QPushButton("Calcular", self)
        self.btn_calcular_nf.setFixedWidth(120)

        self.btn_guardar_nf = QPushButton("Guardar", self)
        self.btn_calcular_nf.setFixedWidth(120)

        hlyt_fecha = QHBoxLayout()
        hlyt_fila_cmbx = QHBoxLayout()
        hlyt_fila_lectura = QHBoxLayout()
        hlyt_fila_resultado = QHBoxLayout()
        hlyt_fila_btns = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila_cmbx.addWidget(self.lbl_freatimetro)
        hlyt_fila_cmbx.addWidget(self.cmbx_freatimetro)

        hlyt_fila_lectura.addWidget(self.lbl_lectura)
        hlyt_fila_lectura.addWidget(self.lned_lectura_f)

        hlyt_fila_resultado.addWidget(self.lbl_Nf)
        hlyt_fila_resultado.addWidget(self.lbl_resultado)
        hlyt_fila_resultado.addWidget(self.lbl_msnm)

        hlyt_fila_btns.addWidget(self.btn_calcular_nf)
        hlyt_fila_btns.addWidget(self.btn_guardar_nf)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_fila_cmbx)
        vlyt_principal.addLayout(hlyt_fila_lectura)
        vlyt_principal.addLayout(hlyt_fila_resultado)
        vlyt_principal.addLayout(hlyt_fila_btns)

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