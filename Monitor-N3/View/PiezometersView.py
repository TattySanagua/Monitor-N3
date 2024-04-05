from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit
import Calculadora

class PiezometersView(QWidget):
    def __init__(self):
        super(PiezometersView, self).__init__()
        self.setup_ui()

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_nivel_embalse = QLabel("Nivel de embalse", self)
        lbl_msnm = QLabel("[msnm]")
        lbl_titulo_piezometro = QLabel("Piezómetros", self)
        lbl_formula_piezometro = QLabel("Np = CB - [(-cos α) * L]", self)
        lbl_descripcion1 = QLabel("Np: Nivel piezométrico [msnm]", self)
        lbl_descripcion2 = QLabel("CB: Cota superior del tubo de elevación [msnm]", self)
        lbl_descripcion3 = QLabel("L: Lectura registrada con sonda electroacústica [m]", self)
        lbl_descripcion4 = QLabel("α: Ángulo cenital de instalación [°], α = 180°", self)

        lbl_piezometro1 = QLabel("L3-PC1", self)
        lbl_piezometro1.setFixedWidth(60)
        lbl_piezometro2 = QLabel("L3-PC2", self)
        lbl_piezometro2.setFixedWidth(60)
        lbl_piezometro3 = QLabel("L3-PC3", self)
        lbl_piezometro3.setFixedWidth(60)
        lbl_piezometro4 = QLabel("L3-PC4", self)
        lbl_piezometro4.setFixedWidth(60)
        lbl_piezometro5 = QLabel("L3-PC5", self)
        lbl_piezometro5.setFixedWidth(60)
        lbl_piezometro6 = QLabel("L3-PC6", self)
        lbl_piezometro6.setFixedWidth(60)
        lbl_piezometro7 = QLabel("L3-PC7", self)
        lbl_piezometro7.setFixedWidth(60)
        self.lbl_Np1 = QLabel("Np1 = 0.0")
        self.lbl_Np2 = QLabel("Np2 = 0.0")
        self.lbl_Np3 = QLabel("Np3 = 0.0")
        self.lbl_Np4 = QLabel("Np4 = 0.0")
        self.lbl_Np5 = QLabel("Np5 = 0.0")
        self.lbl_Np6 = QLabel("Np6 = 0.0")
        self.lbl_Np7 = QLabel("Np7 = 0.0")

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_nivel_embalse = QLineEdit(self)
        self.lned_lectura_p1 = QLineEdit(self)
        self.lned_lectura_p1.setPlaceholderText("Lectura L1")
        self.lned_lectura_p1.setFixedWidth(200)
        self.lned_lectura_p2 = QLineEdit(self)
        self.lned_lectura_p2.setPlaceholderText("Lectura L2")
        self.lned_lectura_p2.setFixedWidth(200)
        self.lned_lectura_p3 = QLineEdit(self)
        self.lned_lectura_p3.setPlaceholderText("Lectura L3")
        self.lned_lectura_p3.setFixedWidth(200)
        self.lned_lectura_p4 = QLineEdit(self)
        self.lned_lectura_p4.setPlaceholderText("Lectura L4")
        self.lned_lectura_p4.setFixedWidth(200)
        self.lned_lectura_p5 = QLineEdit(self)
        self.lned_lectura_p5.setPlaceholderText("Lectura L5")
        self.lned_lectura_p5.setFixedWidth(200)
        self.lned_lectura_p6 = QLineEdit(self)
        self.lned_lectura_p6.setPlaceholderText("Lectura L6")
        self.lned_lectura_p6.setFixedWidth(200)
        self.lned_lectura_p7 = QLineEdit(self)
        self.lned_lectura_p7.setPlaceholderText("Lectura L7")
        self.lned_lectura_p7.setFixedWidth(200)

        self.btn_calcular_np1 = QPushButton("Calcular", self)
        self.btn_calcular_np2 = QPushButton("Calcular", self)
        self.btn_calcular_np3 = QPushButton("Calcular", self)
        self.btn_calcular_np4 = QPushButton("Calcular", self)
        self.btn_calcular_np5 = QPushButton("Calcular", self)
        self.btn_calcular_np6 = QPushButton("Calcular", self)
        self.btn_calcular_np7 = QPushButton("Calcular", self)
        self.btn_guardar_np1 = QPushButton("Guardar registro", self)

        hlyt_fecha = QHBoxLayout()
        hlyt_embalse = QHBoxLayout()
        hlyt_formula_descripcion = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()
        hlyt_fila2 = QHBoxLayout()
        hlyt_fila3 = QHBoxLayout()
        hlyt_fila4 = QHBoxLayout()
        hlyt_fila5 = QHBoxLayout()
        hlyt_fila6 = QHBoxLayout()
        hlyt_fila7 = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_embalse.addWidget(lbl_nivel_embalse)
        hlyt_embalse.addWidget(self.lned_nivel_embalse)
        hlyt_embalse.addWidget(lbl_msnm)

        hlyt_fila1.addWidget(lbl_piezometro1)
        hlyt_fila1.addWidget(self.lned_lectura_p1)
        hlyt_fila1.addWidget(self.btn_calcular_np1)
        hlyt_fila1.addWidget(self.lbl_Np1)
        hlyt_fila1.addWidget(self.btn_guardar_np1)

        hlyt_fila2.addWidget(lbl_piezometro2)
        hlyt_fila2.addWidget(self.lned_lectura_p2)
        hlyt_fila2.addWidget(self.btn_calcular_np2)
        hlyt_fila2.addWidget(self.lbl_Np2)

        hlyt_fila3.addWidget(lbl_piezometro3)
        hlyt_fila3.addWidget(self.lned_lectura_p3)
        hlyt_fila3.addWidget(self.btn_calcular_np3)
        hlyt_fila3.addWidget(self.lbl_Np3)

        hlyt_fila4.addWidget(lbl_piezometro4)
        hlyt_fila4.addWidget(self.lned_lectura_p4)
        hlyt_fila4.addWidget(self.btn_calcular_np4)
        hlyt_fila4.addWidget(self.lbl_Np4)

        hlyt_fila5.addWidget(lbl_piezometro5)
        hlyt_fila5.addWidget(self.lned_lectura_p5)
        hlyt_fila5.addWidget(self.btn_calcular_np5)
        hlyt_fila5.addWidget(self.lbl_Np5)

        hlyt_fila6.addWidget(lbl_piezometro6)
        hlyt_fila6.addWidget(self.lned_lectura_p6)
        hlyt_fila6.addWidget(self.btn_calcular_np6)
        hlyt_fila6.addWidget(self.lbl_Np6)

        hlyt_fila7.addWidget(lbl_piezometro7)
        hlyt_fila7.addWidget(self.lned_lectura_p7)
        hlyt_fila7.addWidget(self.btn_calcular_np7)
        hlyt_fila7.addWidget(self.lbl_Np7)

        vlyt_descripcion = QVBoxLayout()
        vlyt_descripcion.addWidget(lbl_descripcion1)
        vlyt_descripcion.addWidget(lbl_descripcion2)
        vlyt_descripcion.addWidget(lbl_descripcion3)
        vlyt_descripcion.addWidget(lbl_descripcion4)

        hlyt_formula_descripcion.addWidget(lbl_formula_piezometro)
        hlyt_formula_descripcion.addLayout(vlyt_descripcion)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_embalse)
        vlyt_principal.addWidget(lbl_titulo_piezometro, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_formula_descripcion)
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila2)
        vlyt_principal.addLayout(hlyt_fila3)
        vlyt_principal.addLayout(hlyt_fila4)
        vlyt_principal.addLayout(hlyt_fila5)
        vlyt_principal.addLayout(hlyt_fila6)
        vlyt_principal.addLayout(hlyt_fila7)

        self.btn_calcular_np1.clicked.connect(self.calcular_np1)
        self.btn_calcular_np2.clicked.connect(self.calcular_np2)
        self.btn_calcular_np3.clicked.connect(self.calcular_np3)
        self.btn_calcular_np4.clicked.connect(self.calcular_np4)
        self.btn_calcular_np5.clicked.connect(self.calcular_np5)
        self.btn_calcular_np6.clicked.connect(self.calcular_np6)
        self.btn_calcular_np7.clicked.connect(self.calcular_np7)


    def calcular_np1(self):
        cb = 605.22
        lectura = self.lned_lectura_p1.text()

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
            self.lbl_Np1.setText(f"Np1 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()

    def calcular_np2(self):
        cb = 604.24
        lectura = self.lned_lectura_p2.text()

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
            self.lbl_Np2.setText(f"Np2 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()

    def calcular_np3(self):
        cb = 603.88
        lectura = self.lned_lectura_p3.text()

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
            self.lbl_Np3.setText(f"Np3 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()

    def calcular_np4(self):
        cb = 600.60
        lectura = self.lned_lectura_p4.text()

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
            self.lbl_Np4.setText(f"Np4 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()

    def calcular_np5(self):
        cb = 616.32
        lectura = self.lned_lectura_p5.text()

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
            self.lbl_Np5.setText(f"Np5 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()

    def calcular_np6(self):
        cb = 616.17
        lectura = self.lned_lectura_p6.text()

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
            self.lbl_Np6.setText(f"Np6 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()

    def calcular_np7(self):
        cb = 616.02
        lectura = self.lned_lectura_p7.text()

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
            self.lbl_Np7.setText(f"Np7 = {resultado} msnm")
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Valor ingresado no válido. Debe ser un valor numérico.")
            error_dialog.exec_()