from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt
import Calculadora
import sys

class Monitor(QWidget):

    def __init__(self):
        super(Monitor, self).__init__()
        self.setWindowTitle("Monitor N3")
        screen_size = QDesktopWidget().screenGeometry()
        self.setGeometry(50, 50, 700, 650)
        self.display_widgets()

    def display_widgets(self):
        #Etiquetas
        #Piezómetros
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

        #Freatímetro
        lbl_titulo_freatimetro = QLabel("Freatímetro", self)
        lbl_freatimetro = QLabel("L3-F1", self)
        lbl_freatimetro.setFixedWidth(60)
        self.lbl_Nf = QLabel("Nf = 0.0")
        #Aforadores
        lbl_titulo_aforadores = QLabel("Aforadores", self)
        lbl_formula_aforador = QLabel("Caudal Q [l/seg] = Volumen/Tiempo", self)
        lbl_aforador1 = QLabel("AFo3-EI", self)
        lbl_aforador1.setFixedWidth(100)
        lbl_aforador2 = QLabel("AFo3-TOT", self)
        lbl_aforador2.setFixedWidth(100)
        lbl_aforador3 = QLabel("AFo3-PP", self)
        lbl_aforador3.setFixedWidth(100)
        lbl_aforador4 = QLabel("Canaleta Parshall", self)
        lbl_aforador4.setFixedWidth(100)
        self.lbl_caudal1 = QLabel("Q = 0.0")
        self.lbl_caudal2 = QLabel("Q = 0.0")
        self.lbl_caudal3 = QLabel("Q = 0.0")
        self.lbl_caudal4 = QLabel("Q = 0.0")


        #Line Edit
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
        self.lned_lectura_f = QLineEdit(self)
        self.lned_lectura_f.setPlaceholderText("Lectura freatímetro")
        self.lned_lectura_f.setFixedWidth(200)
        self.lned_volumen1 = QLineEdit(self)
        self.lned_volumen1.setPlaceholderText("Volumen")
        self.lned_volumen2 = QLineEdit(self)
        self.lned_volumen2.setPlaceholderText("Volumen")
        self.lned_volumen3 = QLineEdit(self)
        self.lned_volumen3.setPlaceholderText("Volumen")
        self.lned_volumen4 = QLineEdit(self)
        self.lned_volumen4.setPlaceholderText("Volumen")
        self.lned_tiempo1 = QLineEdit(self)
        self.lned_tiempo1.setPlaceholderText("Tiempo")
        self.lned_tiempo2 = QLineEdit(self)
        self.lned_tiempo2.setPlaceholderText("Tiempo")
        self.lned_tiempo3 = QLineEdit(self)
        self.lned_tiempo3.setPlaceholderText("Tiempo")
        self.lned_tiempo4 = QLineEdit(self)
        self.lned_tiempo4.setPlaceholderText("Tiempo")

        #Botones
        self.btn_calcular_np1 = QPushButton("Calcular", self)
        self.btn_calcular_np2 = QPushButton("Calcular", self)
        self.btn_calcular_np3 = QPushButton("Calcular", self)
        self.btn_calcular_np4 = QPushButton("Calcular", self)
        self.btn_calcular_np5 = QPushButton("Calcular", self)
        self.btn_calcular_np6 = QPushButton("Calcular", self)
        self.btn_calcular_np7 = QPushButton("Calcular", self)
        self.btn_calcular_nf = QPushButton("Calcular", self)
        self.btn_calcular_q1 = QPushButton("Calcular", self)
        self.btn_calcular_q2 = QPushButton("Calcular", self)
        self.btn_calcular_q3 = QPushButton("Calcular", self)
        self.btn_calcular_q4 = QPushButton("Calcular", self)

        #Diseños horizontales
        hlyt_formula_descripcion = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()
        hlyt_fila2 = QHBoxLayout()
        hlyt_fila3 = QHBoxLayout()
        hlyt_fila4 = QHBoxLayout()
        hlyt_fila5 = QHBoxLayout()
        hlyt_fila6 = QHBoxLayout()
        hlyt_fila7 = QHBoxLayout()
        hlyt_fila8 = QHBoxLayout()
        hlyt_fila9 = QHBoxLayout()
        hlyt_fila10 = QHBoxLayout()
        hlyt_fila11= QHBoxLayout()
        hlyt_fila12 = QHBoxLayout()

        hlyt_fila1.addWidget(lbl_piezometro1)
        hlyt_fila1.addWidget(self.lned_lectura_p1)
        hlyt_fila1.addWidget(self.btn_calcular_np1)
        hlyt_fila1.addWidget(self.lbl_Np1)

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

        hlyt_fila8.addWidget(lbl_freatimetro)
        hlyt_fila8.addWidget(self.lned_lectura_f)
        hlyt_fila8.addWidget(self.btn_calcular_nf)
        hlyt_fila8.addWidget(self.lbl_Nf)

        hlyt_fila9.addWidget(lbl_aforador1)
        hlyt_fila9.addWidget(self.lned_volumen1)
        hlyt_fila9.addWidget(self.lned_tiempo1)
        hlyt_fila9.addWidget(self.btn_calcular_q1)
        hlyt_fila9.addWidget(self.lbl_caudal1)

        hlyt_fila10.addWidget(lbl_aforador2)
        hlyt_fila10.addWidget(self.lned_volumen2)
        hlyt_fila10.addWidget(self.lned_tiempo2)
        hlyt_fila10.addWidget(self.btn_calcular_q2)
        hlyt_fila10.addWidget(self.lbl_caudal2)

        hlyt_fila11.addWidget(lbl_aforador3)
        hlyt_fila11.addWidget(self.lned_volumen3)
        hlyt_fila11.addWidget(self.lned_tiempo3)
        hlyt_fila11.addWidget(self.btn_calcular_q3)
        hlyt_fila11.addWidget(self.lbl_caudal3)

        hlyt_fila12.addWidget(lbl_aforador4)
        hlyt_fila12.addWidget(self.lned_volumen4)
        hlyt_fila12.addWidget(self.lned_tiempo4)
        hlyt_fila12.addWidget(self.btn_calcular_q4)
        hlyt_fila12.addWidget(self.lbl_caudal4)

        #Diseños verticales
        vlyt_descripcion = QVBoxLayout()
        vlyt_descripcion.addWidget(lbl_descripcion1)
        vlyt_descripcion.addWidget(lbl_descripcion2)
        vlyt_descripcion.addWidget(lbl_descripcion3)
        vlyt_descripcion.addWidget(lbl_descripcion4)

        hlyt_formula_descripcion.addWidget(lbl_formula_piezometro)
        hlyt_formula_descripcion.addLayout(vlyt_descripcion)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(lbl_titulo_piezometro, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_formula_descripcion)
        vlyt_principal.addStretch()
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila2)
        vlyt_principal.addLayout(hlyt_fila3)
        vlyt_principal.addLayout(hlyt_fila4)
        vlyt_principal.addLayout(hlyt_fila5)
        vlyt_principal.addLayout(hlyt_fila6)
        vlyt_principal.addLayout(hlyt_fila7)
        vlyt_principal.addStretch()
        vlyt_principal.addWidget(lbl_titulo_freatimetro, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fila8)
        vlyt_principal.addStretch()
        vlyt_principal.addWidget(lbl_titulo_aforadores, alignment=Qt.AlignCenter)
        vlyt_principal.addWidget(lbl_formula_aforador, alignment=Qt.AlignCenter)
        vlyt_principal.addStretch()
        vlyt_principal.addLayout(hlyt_fila9)
        vlyt_principal.addLayout(hlyt_fila10)
        vlyt_principal.addLayout(hlyt_fila11)
        vlyt_principal.addLayout(hlyt_fila12)

        #Connects
        self.btn_calcular_np1.clicked.connect(self.calcular_np1)
        self.btn_calcular_np2.clicked.connect(self.calcular_np2)
        self.btn_calcular_np3.clicked.connect(self.calcular_np3)
        self.btn_calcular_np4.clicked.connect(self.calcular_np4)
        self.btn_calcular_np5.clicked.connect(self.calcular_np5)
        self.btn_calcular_np6.clicked.connect(self.calcular_np6)
        self.btn_calcular_np7.clicked.connect(self.calcular_np7)
        self.btn_calcular_nf.clicked.connect(self.calcular_nf)
        self.btn_calcular_q1.clicked.connect(self.calcular_q1)
        self.btn_calcular_q2.clicked.connect(self.calcular_q2)
        self.btn_calcular_q3.clicked.connect(self.calcular_q3)
        self.btn_calcular_q4.clicked.connect(self.calcular_q4)

    def calcular_np1(self):
        cb = 605.22
        lectura = float(self.lned_lectura_p1.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np1.setText(f"Np1 = {resultado} msnm")

    def calcular_np2(self):
        cb = 604.24
        lectura = float(self.lned_lectura_p2.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np2.setText(f"Np2 = {resultado} msnm")
    def calcular_np3(self):
        cb = 603.88
        lectura = float(self.lned_lectura_p3.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np3.setText(f"Np3 = {resultado} msnm")
    def calcular_np4(self):
        cb = 600.60
        lectura = float(self.lned_lectura_p4.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np4.setText(f"Np4 = {resultado} msnm")
    def calcular_np5(self):
        cb = 616.32
        lectura = float(self.lned_lectura_p5.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np5.setText(f"Np5 = {resultado} msnm")
    def calcular_np6(self):
        cb = 616.17
        lectura = float(self.lned_lectura_p6.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np6.setText(f"Np6 = {resultado} msnm")
    def calcular_np7(self):
        cb = 616.02
        lectura = float(self.lned_lectura_p7.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Np7.setText(f"Np7 = {resultado} msnm")
    def calcular_nf(self):
        cb = 599.07
        lectura = float(self.lned_lectura_nf.text())
        resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
        self.lbl_Nf.setText(f"Nf = {resultado} msnm")
    def calcular_q1(self):
        volumen = float(self.lned_volumen1.text())
        tiempo = float(self.lned_tiempo1.text())
        resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
        self.lbl_caudal1.setText(f"Q = {resultado} l/seg")
    def calcular_q2(self):
        volumen = float(self.lned_volumen2.text())
        tiempo = float(self.lned_tiempo2.text())
        resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
        self.lbl_caudal2.setText(f"Q = {resultado} l/seg")
    def calcular_q3(self):
        volumen = float(self.lned_volumen3.text())
        tiempo = float(self.lned_tiempo3.text())
        resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
        self.lbl_caudal3.setText(f"Q = {resultado} l/seg")
    def calcular_q4(self):
        volumen = float(self.lned_volumen4.text())
        tiempo = float(self.lned_tiempo4.text())
        resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
        self.lbl_caudal4.setText(f"Q = {resultado} l/seg")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Monitor()
    window.show()
    sys.exit(app.exec_())