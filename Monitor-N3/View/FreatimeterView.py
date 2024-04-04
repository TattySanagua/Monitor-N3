from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox
import Calculadora

class FreatimeterView(QWidget):

    def __init__(self):
        super(FreatimeterView, self).__init__()
        self.setup_ui()

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_nivel_embalse = QLabel("Nivel de embalse", self)
        lbl_titulo_freatimetro = QLabel("Freatímetro", self)
        lbl_freatimetro = QLabel("L3-F1", self)
        lbl_freatimetro.setFixedWidth(60)
        self.lbl_Nf = QLabel("Nf = 0.0")

        self.datetime_edit = QDateTimeEdit(self)
        self.datetime_edit.setCalendarPopup(True)
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())

        self.lned_nivel_embalse = QLineEdit(self)
        self.lned_lectura_f = QLineEdit(self)
        self.lned_lectura_f.setPlaceholderText("Lectura freatímetro")
        self.lned_lectura_f.setFixedWidth(200)

        self.btn_calcular_nf = QPushButton("Calcular", self)

        hlyt_fecha = QHBoxLayout()
        hlyt_embalse = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.datetime_edit)

        hlyt_embalse.addWidget(lbl_nivel_embalse)
        hlyt_embalse.addWidget(self.lned_nivel_embalse)

        hlyt_fila1.addWidget(lbl_freatimetro)
        hlyt_fila1.addWidget(self.lned_lectura_f)
        hlyt_fila1.addWidget(self.btn_calcular_nf)
        hlyt_fila1.addWidget(self.lbl_Nf)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_embalse)
        vlyt_principal.addWidget(lbl_titulo_freatimetro, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fila1)

        self.btn_calcular_nf.clicked.connect(self.calcular_nf)

    def calcular_nf(self):
        cb = 599.07
        lectura = self.lned_lectura_f.text()

        if not lectura:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Por favor, ingrese un valor numérico.")
            error_dialog.exec_()
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_Nf.setText(f"Nf = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()