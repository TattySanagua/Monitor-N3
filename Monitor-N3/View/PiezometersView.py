from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit
from mysql.connector import IntegrityError

import Calculadora
from DataBase.Query import Query

class PiezometersView(QWidget):
    def __init__(self):
        super(PiezometersView, self).__init__()
        self.setup_ui()

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(60)
        lbl_titulo_piezometro = QLabel("Piezómetros", self)
        # lbl_formula_piezometro = QLabel("Np = CB - [(-cos α) * L]", self)
        # lbl_descripcion1 = QLabel("Np: Nivel piezométrico [msnm]", self)
        # lbl_descripcion2 = QLabel("CB: Cota superior del tubo de elevación [msnm]", self)
        # lbl_descripcion3 = QLabel("L: Lectura registrada con sonda electroacústica [m]", self)
        # lbl_descripcion4 = QLabel("α: Ángulo cenital de instalación [°], α = 180°", self)

        lbl_piezometro1 = QLabel("L3-PC1:", self)
        lbl_piezometro1.setFixedWidth(60)
        lbl_piezometro2 = QLabel("L3-PC2:", self)
        lbl_piezometro2.setFixedWidth(60)
        lbl_piezometro3 = QLabel("L3-PC3:", self)
        lbl_piezometro3.setFixedWidth(60)
        lbl_piezometro4 = QLabel("L3-PC4:", self)
        lbl_piezometro4.setFixedWidth(60)
        lbl_piezometro5 = QLabel("L3-PC5:", self)
        lbl_piezometro5.setFixedWidth(60)
        lbl_piezometro6 = QLabel("L3-PC6:", self)
        lbl_piezometro6.setFixedWidth(60)
        lbl_piezometro7 = QLabel("L3-PC7:", self)
        lbl_piezometro7.setFixedWidth(60)
        #
        self.lbl_Np1 = QLabel("Np1 = ")
        self.lbl_Np1.setFixedWidth(60)
        self.lbl_resultado1 = QLabel("")
        self.lbl_resultado1.setFixedWidth(100)
        self.lbl_msnm1 = QLabel("msnm")
        self.lbl_msnm1.setFixedWidth(55)
        #
        self.lbl_Np2 = QLabel("Np2 = ")
        self.lbl_Np2.setFixedWidth(60)
        self.lbl_resultado2 = QLabel("")
        self.lbl_resultado2.setFixedWidth(100)
        self.lbl_msnm2 = QLabel("msnm")
        self.lbl_msnm2.setFixedWidth(55)
        #
        self.lbl_Np3 = QLabel("Np3 = ")
        self.lbl_Np3.setFixedWidth(60)
        self.lbl_resultado3 = QLabel("")
        self.lbl_resultado3.setFixedWidth(100)
        self.lbl_msnm3 = QLabel("msnm")
        self.lbl_msnm3.setFixedWidth(55)
        #
        self.lbl_Np4 = QLabel("Np4 = ")
        self.lbl_Np4.setFixedWidth(60)
        self.lbl_resultado4 = QLabel("")
        self.lbl_resultado4.setFixedWidth(100)
        self.lbl_msnm4 = QLabel("msnm")
        self.lbl_msnm4.setFixedWidth(55)
        #
        self.lbl_Np5 = QLabel("Np5 = ")
        self.lbl_Np5.setFixedWidth(60)
        self.lbl_resultado5 = QLabel("")
        self.lbl_resultado5.setFixedWidth(100)
        self.lbl_msnm5 = QLabel("msnm")
        self.lbl_msnm5.setFixedWidth(55)
        #
        self.lbl_Np6 = QLabel("Np6 = ")
        self.lbl_Np6.setFixedWidth(60)
        self.lbl_resultado6 = QLabel("")
        self.lbl_resultado6.setFixedWidth(100)
        self.lbl_msnm6 = QLabel("msnm")
        self.lbl_msnm6.setFixedWidth(55)
        #
        self.lbl_Np7 = QLabel("Np7 = ")
        self.lbl_Np7.setFixedWidth(60)
        self.lbl_resultado7 = QLabel("")
        self.lbl_resultado7.setFixedWidth(100)
        self.lbl_msnm7 = QLabel("msnm")
        self.lbl_msnm7.setFixedWidth(55)

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_lectura_p1 = QLineEdit(self)
        self.lned_lectura_p1.setPlaceholderText("Lectura L1")
        self.lned_lectura_p1.setFixedWidth(160)
        self.lned_lectura_p2 = QLineEdit(self)
        self.lned_lectura_p2.setPlaceholderText("Lectura L2")
        self.lned_lectura_p2.setFixedWidth(160)
        self.lned_lectura_p3 = QLineEdit(self)
        self.lned_lectura_p3.setPlaceholderText("Lectura L3")
        self.lned_lectura_p3.setFixedWidth(160)
        self.lned_lectura_p4 = QLineEdit(self)
        self.lned_lectura_p4.setPlaceholderText("Lectura L4")
        self.lned_lectura_p4.setFixedWidth(160)
        self.lned_lectura_p5 = QLineEdit(self)
        self.lned_lectura_p5.setPlaceholderText("Lectura L5")
        self.lned_lectura_p5.setFixedWidth(160)
        self.lned_lectura_p6 = QLineEdit(self)
        self.lned_lectura_p6.setPlaceholderText("Lectura L6")
        self.lned_lectura_p6.setFixedWidth(160)
        self.lned_lectura_p7 = QLineEdit(self)
        self.lned_lectura_p7.setPlaceholderText("Lectura L7")
        self.lned_lectura_p7.setFixedWidth(160)

        self.btn_calcular_np1 = QPushButton("Calcular", self)
        self.btn_calcular_np1.setFixedWidth(120)
        self.btn_calcular_np2 = QPushButton("Calcular", self)
        self.btn_calcular_np2.setFixedWidth(120)
        self.btn_calcular_np3 = QPushButton("Calcular", self)
        self.btn_calcular_np3.setFixedWidth(120)
        self.btn_calcular_np4 = QPushButton("Calcular", self)
        self.btn_calcular_np4.setFixedWidth(120)
        self.btn_calcular_np5 = QPushButton("Calcular", self)
        self.btn_calcular_np5.setFixedWidth(120)
        self.btn_calcular_np6 = QPushButton("Calcular", self)
        self.btn_calcular_np6.setFixedWidth(120)
        self.btn_calcular_np7 = QPushButton("Calcular", self)
        self.btn_calcular_np7.setFixedWidth(120)
        self.btn_guardar_np1 = QPushButton("Guardar Np1", self)
        self.btn_guardar_np1.setFixedWidth(120)
        self.btn_guardar_np2 = QPushButton("Guardar Np2", self)
        self.btn_guardar_np2.setFixedWidth(120)
        self.btn_guardar_np3 = QPushButton("Guardar Np3", self)
        self.btn_guardar_np3.setFixedWidth(120)
        self.btn_guardar_np4 = QPushButton("Guardar Np4", self)
        self.btn_guardar_np4.setFixedWidth(120)
        self.btn_guardar_np5 = QPushButton("Guardar Np5", self)
        self.btn_guardar_np5.setFixedWidth(120)
        self.btn_guardar_np6 = QPushButton("Guardar Np6", self)
        self.btn_guardar_np6.setFixedWidth(120)
        self.btn_guardar_np7 = QPushButton("Guardar Np7", self)
        self.btn_guardar_np7.setFixedWidth(120)

        hlyt_fecha = QHBoxLayout()
        #hlyt_formula_descripcion = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()
        hlyt_fila1a = QHBoxLayout()
        hlyt_fila2 = QHBoxLayout()
        hlyt_fila2a = QHBoxLayout()
        hlyt_fila3 = QHBoxLayout()
        hlyt_fila3a = QHBoxLayout()
        hlyt_fila4 = QHBoxLayout()
        hlyt_fila4a = QHBoxLayout()
        hlyt_fila5 = QHBoxLayout()
        hlyt_fila5a = QHBoxLayout()
        hlyt_fila6 = QHBoxLayout()
        hlyt_fila6a = QHBoxLayout()
        hlyt_fila7 = QHBoxLayout()
        hlyt_fila7a = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila1.addWidget(lbl_piezometro1)
        hlyt_fila1.addWidget(self.lned_lectura_p1)
        hlyt_fila1.addWidget(self.btn_calcular_np1)
        hlyt_fila1a.addWidget(self.lbl_Np1)
        hlyt_fila1a.addWidget(self.lbl_resultado1)
        hlyt_fila1a.addWidget(self.lbl_msnm1)
        hlyt_fila1a.addWidget(self.btn_guardar_np1)

        hlyt_fila2.addWidget(lbl_piezometro2)
        hlyt_fila2.addWidget(self.lned_lectura_p2)
        hlyt_fila2.addWidget(self.btn_calcular_np2)
        hlyt_fila2a.addWidget(self.lbl_Np2)
        hlyt_fila2a.addWidget(self.lbl_resultado2)
        hlyt_fila2a.addWidget(self.lbl_msnm2)
        hlyt_fila2a.addWidget(self.btn_guardar_np2)

        hlyt_fila3.addWidget(lbl_piezometro3)
        hlyt_fila3.addWidget(self.lned_lectura_p3)
        hlyt_fila3.addWidget(self.btn_calcular_np3)
        hlyt_fila3a.addWidget(self.lbl_Np3)
        hlyt_fila3a.addWidget(self.lbl_resultado3)
        hlyt_fila3a.addWidget(self.lbl_msnm3)
        hlyt_fila3a.addWidget(self.btn_guardar_np3)

        hlyt_fila4.addWidget(lbl_piezometro4)
        hlyt_fila4.addWidget(self.lned_lectura_p4)
        hlyt_fila4.addWidget(self.btn_calcular_np4)
        hlyt_fila4a.addWidget(self.lbl_Np4)
        hlyt_fila4a.addWidget(self.lbl_resultado4)
        hlyt_fila4a.addWidget(self.lbl_msnm4)
        hlyt_fila4a.addWidget(self.btn_guardar_np4)

        hlyt_fila5.addWidget(lbl_piezometro5)
        hlyt_fila5.addWidget(self.lned_lectura_p5)
        hlyt_fila5.addWidget(self.btn_calcular_np5)
        hlyt_fila5a.addWidget(self.lbl_Np5)
        hlyt_fila5a.addWidget(self.lbl_resultado5)
        hlyt_fila5a.addWidget(self.lbl_msnm5)
        hlyt_fila5a.addWidget(self.btn_guardar_np5)

        hlyt_fila6.addWidget(lbl_piezometro6)
        hlyt_fila6.addWidget(self.lned_lectura_p6)
        hlyt_fila6.addWidget(self.btn_calcular_np6)
        hlyt_fila6a.addWidget(self.lbl_Np6)
        hlyt_fila6a.addWidget(self.lbl_resultado6)
        hlyt_fila6a.addWidget(self.lbl_msnm6)
        hlyt_fila6a.addWidget(self.btn_guardar_np6)

        hlyt_fila7.addWidget(lbl_piezometro7)
        hlyt_fila7.addWidget(self.lned_lectura_p7)
        hlyt_fila7.addWidget(self.btn_calcular_np7)
        hlyt_fila7a.addWidget(self.lbl_Np7)
        hlyt_fila7a.addWidget(self.lbl_resultado7)
        hlyt_fila7a.addWidget(self.lbl_msnm7)
        hlyt_fila7a.addWidget(self.btn_guardar_np7)

        # vlyt_descripcion = QVBoxLayout()
        # vlyt_descripcion.addWidget(lbl_descripcion1)
        # vlyt_descripcion.addWidget(lbl_descripcion2)
        # vlyt_descripcion.addWidget(lbl_descripcion3)
        # vlyt_descripcion.addWidget(lbl_descripcion4)
        #
        # hlyt_formula_descripcion.addWidget(lbl_formula_piezometro)
        # hlyt_formula_descripcion.addLayout(vlyt_descripcion)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addWidget(lbl_titulo_piezometro, alignment=Qt.AlignCenter)
        # vlyt_principal.addLayout(hlyt_formula_descripcion)
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila1a)
        vlyt_principal.addLayout(hlyt_fila2)
        vlyt_principal.addLayout(hlyt_fila2a)
        vlyt_principal.addLayout(hlyt_fila3)
        vlyt_principal.addLayout(hlyt_fila3a)
        vlyt_principal.addLayout(hlyt_fila4)
        vlyt_principal.addLayout(hlyt_fila4a)
        vlyt_principal.addLayout(hlyt_fila5)
        vlyt_principal.addLayout(hlyt_fila5a)
        vlyt_principal.addLayout(hlyt_fila6)
        vlyt_principal.addLayout(hlyt_fila6a)
        vlyt_principal.addLayout(hlyt_fila7)
        vlyt_principal.addLayout(hlyt_fila7a)

        self.btn_calcular_np1.clicked.connect(self.calcular_np1)
        self.btn_calcular_np2.clicked.connect(self.calcular_np2)
        self.btn_calcular_np3.clicked.connect(self.calcular_np3)
        self.btn_calcular_np4.clicked.connect(self.calcular_np4)
        self.btn_calcular_np5.clicked.connect(self.calcular_np5)
        self.btn_calcular_np6.clicked.connect(self.calcular_np6)
        self.btn_calcular_np7.clicked.connect(self.calcular_np7)
        self.btn_guardar_np1.clicked.connect(self.guardar_np1)
        self.btn_guardar_np2.clicked.connect(self.guardar_np2)
        self.btn_guardar_np3.clicked.connect(self.guardar_np3)
        self.btn_guardar_np4.clicked.connect(self.guardar_np4)
        self.btn_guardar_np5.clicked.connect(self.guardar_np5)
        self.btn_guardar_np6.clicked.connect(self.guardar_np6)
        self.btn_guardar_np7.clicked.connect(self.guardar_np7)


    def calcular_np1(self):
        cb = 605.22
        lectura = self.lned_lectura_p1.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado1.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p1.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_np2(self):
        cb = 604.24
        lectura = self.lned_lectura_p2.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado2.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p2.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_np3(self):
        cb = 603.88
        lectura = self.lned_lectura_p3.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado3.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p3.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_np4(self):
        cb = 600.60
        lectura = self.lned_lectura_p4.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado4.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p4.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_np5(self):
        cb = 616.32
        lectura = self.lned_lectura_p5.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado5.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p5.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_np6(self):
        cb = 616.17
        lectura = self.lned_lectura_p6.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado6.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p6.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_np7(self):
        cb = 616.02
        lectura = self.lned_lectura_p7.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un valor numérico.")
            return

        try:
            lectura = float(lectura)
            resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
            self.lbl_resultado7.setText(f"{resultado:.{decimales}f}")
            self.lned_lectura_p7.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def guardar_np1(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado1.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc1(fecha, nivel_piezometrico)
            self.lbl_resultado1.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_np2(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado2.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc2(fecha, nivel_piezometrico)
            self.lbl_resultado2.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_np3(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado3.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc3(fecha, nivel_piezometrico)
            self.lbl_resultado3.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_np4(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado4.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc4(fecha, nivel_piezometrico)
            self.lbl_resultado4.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_np5(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado5.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc5(fecha, nivel_piezometrico)
            self.lbl_resultado5.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_np6(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado6.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc6(fecha, nivel_piezometrico)
            self.lbl_resultado6.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_np7(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        nivel_piezometrico = self.lbl_resultado7.text()

        if not nivel_piezometrico or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o nivel piezométrico.")
            return

        try:
            nivel_piezometrico = float(nivel_piezometrico)
            Query.insert_data_l3_pc7(fecha, nivel_piezometrico)
            self.lbl_resultado7.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")