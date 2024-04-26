from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QDateEdit
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

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(110)
        lbl_titulo_freatimetro = QLabel("Freatímetro", self)
        lbl_freatimetro = QLabel("L3-F1:", self)
        lbl_freatimetro.setFixedWidth(60)
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

        self.lned_lectura_f = QLineEdit(self)
        self.lned_lectura_f.setPlaceholderText("Lectura freatímetro")
        self.lned_lectura_f.setFixedWidth(160)

        self.btn_calcular_nf = QPushButton("Calcular", self)
        self.btn_calcular_nf.setFixedWidth(120)
        self.btn_guardar_nf = QPushButton("Guardar", self)
        self.btn_calcular_nf.setFixedWidth(120)

        hlyt_fecha = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()
        hlyt_fila2 = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila1.addWidget(lbl_freatimetro)
        hlyt_fila1.addWidget(self.lned_lectura_f)
        hlyt_fila1.addWidget(self.btn_calcular_nf)


        hlyt_fila2.addWidget(self.lbl_Nf)
        hlyt_fila2.addWidget(self.lbl_resultado)
        hlyt_fila2.addWidget(self.lbl_msnm)
        hlyt_fila2.addWidget(self.btn_guardar_nf)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addWidget(lbl_titulo_freatimetro, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila2)

        self.data_updater = DataUpdater()

        self.btn_calcular_nf.clicked.connect(self.calcular_nf)
        self.btn_guardar_nf.clicked.connect(self.guardar_nf)
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

    def calcular_nf(self):
        cb = 599.07
        lectura = self.lned_lectura_f.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, complete el campo numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_f.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def guardar_nf(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_freatico = self.lbl_resultado.text()

        if not nivel_freatico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel freatico.")
            return

        try:
            nivel_freatico = float(nivel_freatico)
            Query.insert_data_l3_f1(fecha, nivel_freatico)
            self.lbl_resultado.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
            self.data_updater.update_data()
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def actualizar_tabla(self):
        self.tabla_freatimetro_view.update_table()