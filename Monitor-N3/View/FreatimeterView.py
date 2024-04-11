from PyQt5.QtCore import Qt, QDateTime, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit
import Calculadora

class FreatimeterView(QWidget):

    def __init__(self):
        super(FreatimeterView, self).__init__()
        self.setup_ui()

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
        self.lbl_resultado.setFixedWidth(160)

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
        hlyt_fila2.addWidget(self.btn_guardar_nf)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addWidget(lbl_titulo_freatimetro, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila2)

        self.btn_calcular_nf.clicked.connect(self.calcular_nf)

    def calcular_nf(self):
        cb = 599.07
        lectura = self.lned_lectura_f.text()
        decimales = 2

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
            self.lbl_resultado.setText(f"{resultado:.{decimales}f} msnm")
            self.lned_lectura_f.clear()
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()