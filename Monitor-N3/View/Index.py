from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Monitor(QWidget):

    def __init__(self):
        super(Monitor, self).__init__()
        self.setWindowTitle("Monitor N3")
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
        lbl_piezometro2 = QLabel("L3-PC2", self)
        lbl_piezometro3 = QLabel("L3-PC3", self)
        lbl_piezometro4 = QLabel("L3-PC4", self)
        lbl_piezometro5 = QLabel("L3-PC5", self)
        lbl_piezometro6 = QLabel("L3-PC6", self)
        lbl_piezometro7 = QLabel("L3-PC7", self)
        lbl_Np = QLabel("Np = ", self)

        #Freatímetro
        lbl_titulo_freatimetro = QLabel("Freatímetro", self)
        lbl_freatimetro = QLabel("L3-F1", self)
        lbl_Nf = QLabel("Nf = ", self)
        #Aforadores
        lbl_titulo_aforadores = QLabel("Aforadores", self)
        lbl_formula_aforador = QLabel("Caudal Q [l/seg] = Volumen/Tiempo", self)
        lbl_aforador1 = QLabel("AFo3-EI", self)
        lbl_aforador2 = QLabel("AFo3-TOT", self)
        lbl_aforador3 = QLabel("AFo3-PP", self)
        lbl_aforador4 = QLabel("Canaleta Parshall", self)
        lbl_caudal = QLabel("Q = ", self)

        #Line Edit
        lned_lectura_p1 = QLineEdit(self)
        lned_lectura_p1.setPlaceholderText("Lectura L1")
        lned_lectura_p2 = QLineEdit(self)
        lned_lectura_p2.setPlaceholderText("Lectura L2")
        lned_lectura_p3 = QLineEdit(self)
        lned_lectura_p3.setPlaceholderText("Lectura L3")
        lned_lectura_p4 = QLineEdit(self)
        lned_lectura_p4.setPlaceholderText("Lectura L4")
        lned_lectura_p5 = QLineEdit(self)
        lned_lectura_p5.setPlaceholderText("Lectura L5")
        lned_lectura_p6 = QLineEdit(self)
        lned_lectura_p6.setPlaceholderText("Lectura L6")
        lned_lectura_p7 = QLineEdit(self)
        lned_lectura_p7.setPlaceholderText("Lectura L7")
        lned_lectura_f = QLineEdit(self)
        lned_lectura_f.setPlaceholderText("Lectura freat.")

        #Diseños horizontales
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
        hlyt_fila1.addWidget(lned_lectura_p1)
        hlyt_fila1.addWidget(lbl_Np)

        hlyt_fila2.addWidget(lbl_piezometro2)
        hlyt_fila2.addWidget(lned_lectura_p2)
        hlyt_fila2.addWidget(lbl_Np)

        hlyt_fila3.addWidget(lbl_piezometro3)
        hlyt_fila3.addWidget(lned_lectura_p3)
        hlyt_fila3.addWidget(lbl_Np)

        hlyt_fila4.addWidget(lbl_piezometro4)
        hlyt_fila4.addWidget(lned_lectura_p4)
        hlyt_fila4.addWidget(lbl_Np)

        hlyt_fila5.addWidget(lbl_piezometro5)
        hlyt_fila5.addWidget(lned_lectura_p5)
        hlyt_fila5.addWidget(lbl_Np)

        hlyt_fila6.addWidget(lbl_piezometro6)
        hlyt_fila6.addWidget(lned_lectura_p6)
        hlyt_fila6.addWidget(lbl_Np)

        hlyt_fila7.addWidget(lbl_piezometro7)
        hlyt_fila7.addWidget(lned_lectura_p7)
        hlyt_fila7.addWidget(lbl_Np)

        hlyt_fila8.addWidget(lbl_freatimetro)
        hlyt_fila8.addWidget(lned_lectura_f)
        hlyt_fila8.addWidget(lbl_Nf)

        hlyt_fila9.addWidget(lbl_aforador1)
        hlyt_fila9.addWidget(lbl_caudal)

        hlyt_fila10.addWidget(lbl_aforador2)
        hlyt_fila10.addWidget(lbl_caudal)

        hlyt_fila11.addWidget(lbl_aforador3)
        hlyt_fila11.addWidget(lbl_caudal)

        hlyt_fila12.addWidget(lbl_aforador4)
        hlyt_fila12.addWidget(lbl_caudal)

        #Diseño vertical
        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(lbl_titulo_piezometro)

        vlyt_principal.addWidget(lbl_formula_piezometro)
        vlyt_principal.addWidget(lbl_descripcion1)
        vlyt_principal.addWidget(lbl_descripcion2)
        vlyt_principal.addWidget(lbl_descripcion3)
        vlyt_principal.addWidget(lbl_descripcion4)
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila2)
        vlyt_principal.addLayout(hlyt_fila3)
        vlyt_principal.addLayout(hlyt_fila4)
        vlyt_principal.addLayout(hlyt_fila5)
        vlyt_principal.addLayout(hlyt_fila6)
        vlyt_principal.addLayout(hlyt_fila7)

        vlyt_principal.addWidget(lbl_titulo_freatimetro)
        vlyt_principal.addLayout(hlyt_fila8)

        vlyt_principal.addWidget(lbl_titulo_aforadores)
        vlyt_principal.addWidget(lbl_formula_aforador)
        vlyt_principal.addLayout(hlyt_fila9)
        vlyt_principal.addLayout(hlyt_fila10)
        vlyt_principal.addLayout(hlyt_fila11)
        vlyt_principal.addLayout(hlyt_fila12)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Monitor()
    window.show()
    sys.exit(app.exec_())