from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit
from mysql.connector import IntegrityError

import Calculadora
from DataBase.Query import Query

class AforadoresView(QWidget):

    def __init__(self):
        super(AforadoresView, self).__init__()
        self.setup_ui()

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(60)
        lbl_titulo_aforadores = QLabel("Aforadores", self)
        #lbl_formula_aforador = QLabel("Caudal Q [l/seg] = Volumen/Tiempo", self)
        lbl_aforador1 = QLabel("AFo3-EI:", self)
        lbl_aforador1.setFixedWidth(60)
        lbl_aforador2 = QLabel("AFo3-TOT:", self)
        lbl_aforador2.setFixedWidth(65)
        lbl_aforador3 = QLabel("AFo3-PP:", self)
        lbl_aforador3.setFixedWidth(60)
        lbl_titulo_parshall = QLabel("Aforador Parshall", self)
        lbl_formula_parshall = QLabel("Caudal Q [m3/seg] = K*ha^u", self)
        lbl_descripcion1 = QLabel("Para ancho de garganta de 3 pulgadas, K = 0.1771 y u = 1.55", self)
        lbl_descripcion2 = QLabel("ha: Tirante medido en la zona de convergencia [m]", self)
        lbl_ha = QLabel("ha", self)
        lbl_ha.setFixedWidth(60)
        #
        self.lbl_caudal1 = QLabel("Q1 = ")
        self.lbl_caudal1.setFixedWidth(60)
        self.lbl_resultado1 = QLabel("")
        self.lbl_resultado1.setFixedWidth(100)
        self.lbl_ls1 = QLabel("l/s")
        self.lbl_ls1.setFixedWidth(55)
        #
        self.lbl_caudal2 = QLabel("Q2 = ")
        self.lbl_caudal2.setFixedWidth(60)
        self.lbl_resultado2 = QLabel("")
        self.lbl_resultado2.setFixedWidth(160)
        self.lbl_ls2 = QLabel("l/s")
        self.lbl_ls2.setFixedWidth(55)
        #
        self.lbl_caudal3 = QLabel("Q3 = ")
        self.lbl_caudal3.setFixedWidth(60)
        self.lbl_resultado3 = QLabel("")
        self.lbl_resultado3.setFixedWidth(160)
        self.lbl_ls3 = QLabel("l/s")
        self.lbl_ls3.setFixedWidth(55)
        #
        self.lbl_caudal_parshall = QLabel("Q = ")
        self.lbl_caudal_parshall.setFixedWidth(60)
        self.lbl_resultado4 = QLabel("")
        self.lbl_resultado4.setFixedWidth(100)
        self.lbl_m3s = QLabel("m3/s")
        self.lbl_m3s.setFixedWidth(55)

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_volumen1 = QLineEdit(self)
        self.lned_volumen1.setPlaceholderText("Volumen l")
        self.lned_volumen2 = QLineEdit(self)
        self.lned_volumen2.setPlaceholderText("Volumen l")
        self.lned_volumen3 = QLineEdit(self)
        self.lned_volumen3.setPlaceholderText("Volumen l")
        self.lned_tiempo1 = QLineEdit(self)
        self.lned_tiempo1.setPlaceholderText("Tiempo s")
        self.lned_tiempo2 = QLineEdit(self)
        self.lned_tiempo2.setPlaceholderText("Tiempo s")
        self.lned_tiempo3 = QLineEdit(self)
        self.lned_tiempo3.setPlaceholderText("Tiempo s")
        self.lned_ha = QLineEdit(self)
        self.lned_ha.setFixedWidth(160)

        self.btn_calcular_q1 = QPushButton("Calcular", self)
        self.btn_calcular_q2 = QPushButton("Calcular", self)
        self.btn_calcular_q3 = QPushButton("Calcular", self)
        self.btn_calcular_parshall = QPushButton("Calcular", self)
        self.btn_calcular_parshall.setFixedWidth(120)
        self.btn_guardar_q1 = QPushButton("Guardar Q1", self)
        self.btn_guardar_q1.setFixedWidth(120)
        self.btn_guardar_q2 = QPushButton("Guardar Q2", self)
        self.btn_guardar_q2.setFixedWidth(120)
        self.btn_guardar_q3 = QPushButton("Guardar Q3", self)
        self.btn_guardar_q3.setFixedWidth(120)
        self.btn_guardar_q4 = QPushButton("Guardar Q", self)
        self.btn_guardar_q4.setFixedWidth(120)

        hlyt_fecha = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()
        hlyt_fila1a = QHBoxLayout()
        hlyt_fila2 = QHBoxLayout()
        hlyt_fila2a = QHBoxLayout()
        hlyt_fila3 = QHBoxLayout()
        hlyt_fila3a = QHBoxLayout()
        hlyt_fila4 = QHBoxLayout()
        hlyt_fila4a = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila1.addWidget(lbl_aforador1)
        hlyt_fila1.addWidget(self.lned_volumen1)
        hlyt_fila1.addWidget(self.lned_tiempo1)
        hlyt_fila1.addWidget(self.btn_calcular_q1)

        hlyt_fila1a.addWidget(self.lbl_caudal1)
        hlyt_fila1a.addWidget(self.lbl_resultado1)
        hlyt_fila1a.addWidget(self.lbl_ls1)
        hlyt_fila1a.addWidget(self.btn_guardar_q1)

        hlyt_fila2.addWidget(lbl_aforador2)
        hlyt_fila2.addWidget(self.lned_volumen2)
        hlyt_fila2.addWidget(self.lned_tiempo2)
        hlyt_fila2.addWidget(self.btn_calcular_q2)

        hlyt_fila2a.addWidget(self.lbl_caudal2)
        hlyt_fila2a.addWidget(self.lbl_resultado2)
        hlyt_fila2a.addWidget(self.lbl_ls2)
        hlyt_fila2a.addWidget(self.btn_guardar_q2)

        hlyt_fila3.addWidget(lbl_aforador3)
        hlyt_fila3.addWidget(self.lned_volumen3)
        hlyt_fila3.addWidget(self.lned_tiempo3)
        hlyt_fila3.addWidget(self.btn_calcular_q3)

        hlyt_fila3a.addWidget(self.lbl_caudal3)
        hlyt_fila3a.addWidget(self.lbl_resultado3)
        hlyt_fila3a.addWidget(self.lbl_ls3)
        hlyt_fila3a.addWidget(self.btn_guardar_q3)

        hlyt_fila4.addWidget(lbl_ha)
        hlyt_fila4.addWidget(self.lned_ha)
        hlyt_fila4.addWidget(self.btn_calcular_parshall)

        hlyt_fila4a.addWidget(self.lbl_caudal_parshall)
        hlyt_fila4a.addWidget(self.lbl_resultado4)
        hlyt_fila4a.addWidget(self.lbl_m3s)
        hlyt_fila4a.addWidget(self.btn_guardar_q4)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addWidget(lbl_titulo_aforadores, alignment=Qt.AlignCenter)
        #vlyt_principal.addWidget(lbl_formula_aforador, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fila1)
        vlyt_principal.addLayout(hlyt_fila1a)
        vlyt_principal.addLayout(hlyt_fila2)
        vlyt_principal.addLayout(hlyt_fila2a)
        vlyt_principal.addLayout(hlyt_fila3)
        vlyt_principal.addLayout(hlyt_fila3a)
        vlyt_principal.addWidget(lbl_titulo_parshall, alignment=Qt.AlignCenter)
        vlyt_principal.addWidget(lbl_formula_parshall, alignment=Qt.AlignCenter)
        vlyt_principal.addWidget(lbl_descripcion1, alignment=Qt.AlignCenter)
        vlyt_principal.addWidget(lbl_descripcion2, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fila4)
        vlyt_principal.addLayout(hlyt_fila4a)

        # Connects
        self.btn_calcular_q1.clicked.connect(self.calcular_q1)
        self.btn_calcular_q2.clicked.connect(self.calcular_q2)
        self.btn_calcular_q3.clicked.connect(self.calcular_q3)
        self.btn_calcular_parshall.clicked.connect(self.calcular_q4)
        self.btn_guardar_q1.clicked.connect(self.guardar_q1)
        self.btn_guardar_q2.clicked.connect(self.guardar_q2)
        self.btn_guardar_q3.clicked.connect(self.guardar_q3)
        self.btn_guardar_q4.clicked.connect(self.guardar_q4)

    def calcular_q1(self):
        volumen = self.lned_volumen1.text()
        tiempo = self.lned_tiempo1.text()
        decimales = 2

        if not volumen or not tiempo:
            QMessageBox.warning(self, "Error", "Por favor, complete los campos numéricos.")
            return

        try:
            volumen = float(volumen)
            tiempo = float(tiempo)
            resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
            self.lbl_resultado1.setText(f"{resultado:.{decimales}f}")
            self.lned_volumen1.clear()
            self.lned_tiempo1.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_q2(self):
        volumen = self.lned_volumen2.text()
        tiempo = self.lned_tiempo2.text()
        decimales = 2

        if not volumen or not tiempo:
            QMessageBox.warning(self, "Error", "Por favor, complete los campos numéricos.")
            return

        try:
            volumen = float(volumen)
            tiempo = float(tiempo)
            resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
            self.lbl_resultado2.setText(f"{resultado:.{decimales}f}")
            self.lned_volumen2.clear()
            self.lned_tiempo2.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_q3(self):
        volumen = self.lned_volumen3.text()
        tiempo = self.lned_tiempo3.text()
        decimales = 2

        if not volumen or not tiempo:
            QMessageBox.warning(self, "Error", "Por favor, complete los campos numéricos.")
            return

        try:
            volumen = float(volumen)
            tiempo = float(tiempo)
            resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
            self.lbl_resultado3.setText(f"{resultado:.{decimales}f}")
            self.lned_volumen3.clear()
            self.lned_tiempo3.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def calcular_q4(self):
        ha = self.lned_ha.text()
        decimales = 2

        if not ha:
            QMessageBox.warning(self, "Error", "Por favor, complete los campos numéricos.")
            return

        try:
            ha = float(ha)
            resultado = Calculadora.Calculadora().calcular_caudal_parshall(ha)
            self.lbl_resultado4.setText(f"{resultado:.{decimales}f}")
            self.lned_ha.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def guardar_q1(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        caudal = self.lbl_resultado1.text()

        if not caudal or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o caudal.")
            return

        try:
            caudal = float(caudal)
            Query.insert_data_afo3_ei(fecha, caudal)
            self.lbl_resultado1.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_q2(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        caudal = self.lbl_resultado2.text()

        if not caudal or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o caudal.")
            return

        try:
            caudal = float(caudal)
            Query.insert_data_afo3_tot(fecha, caudal)
            self.lbl_resultado2.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error",
                                 "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_q3(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        caudal = self.lbl_resultado3.text()

        if not caudal or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o caudal.")
            return

        try:
            caudal = float(caudal)
            Query.insert_data_afo3_pp(fecha, caudal)
            self.lbl_resultado3.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error",
                                 "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def guardar_q4(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        caudal = self.lbl_resultado4.text()

        if not caudal or not fecha:
            QMessageBox.warning(self, "Error", "Debe completar los campos de fecha y/o caudal.")
            return

        try:
            caudal = float(caudal)
            Query.insert_data_parshall(fecha, caudal)
            self.lbl_resultado4.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        except ValueError:
            QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
            QMessageBox.critical(self, "Error",
                                 "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")