from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit
from mysql.connector import IntegrityError
from DataBase.Query import Query
from Signals.DataUpdater import DataUpdater
import Calculadora


class AforadoresView(QWidget):

    def __init__(self, tabla_embalse_aforadores):
        super(AforadoresView, self).__init__()
        self.setup_ui()
        self.tabla_embalse_aforadores = tabla_embalse_aforadores
        self.data_updater = DataUpdater()
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(60)
        lbl_titulo_aforadores = QLabel("Aforadores", self)
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

        self.btn_calcular_caudales = QPushButton("Calcular", self)
        self.btn_calcular_caudales.setFixedWidth(120)
        self.btn_guardar_caudales = QPushButton("Guardar", self)
        self.btn_guardar_caudales.setFixedWidth(120)

        hlyt_fecha = QHBoxLayout()
        hlyt_fila1 = QHBoxLayout()
        hlyt_fila1a = QHBoxLayout()
        hlyt_fila2 = QHBoxLayout()
        hlyt_fila2a = QHBoxLayout()
        hlyt_fila3 = QHBoxLayout()
        hlyt_fila3a = QHBoxLayout()
        hlyt_fila4 = QHBoxLayout()
        hlyt_fila4a = QHBoxLayout()
        hlyt_fila5 = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila1.addWidget(lbl_aforador1)
        hlyt_fila1.addWidget(self.lned_volumen1)
        hlyt_fila1.addWidget(self.lned_tiempo1)

        hlyt_fila1a.addWidget(self.lbl_caudal1)
        hlyt_fila1a.addWidget(self.lbl_resultado1)
        hlyt_fila1a.addWidget(self.lbl_ls1)

        hlyt_fila2.addWidget(lbl_aforador2)
        hlyt_fila2.addWidget(self.lned_volumen2)
        hlyt_fila2.addWidget(self.lned_tiempo2)

        hlyt_fila2a.addWidget(self.lbl_caudal2)
        hlyt_fila2a.addWidget(self.lbl_resultado2)
        hlyt_fila2a.addWidget(self.lbl_ls2)

        hlyt_fila3.addWidget(lbl_aforador3)
        hlyt_fila3.addWidget(self.lned_volumen3)
        hlyt_fila3.addWidget(self.lned_tiempo3)

        hlyt_fila3a.addWidget(self.lbl_caudal3)
        hlyt_fila3a.addWidget(self.lbl_resultado3)
        hlyt_fila3a.addWidget(self.lbl_ls3)

        hlyt_fila4.addWidget(lbl_ha)
        hlyt_fila4.addWidget(self.lned_ha)

        hlyt_fila4a.addWidget(self.lbl_caudal_parshall)
        hlyt_fila4a.addWidget(self.lbl_resultado4)
        hlyt_fila4a.addWidget(self.lbl_m3s)

        hlyt_fila5.addWidget(self.btn_calcular_caudales)
        hlyt_fila5.addWidget(self.btn_guardar_caudales)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addWidget(lbl_titulo_aforadores, alignment=Qt.AlignCenter)
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
        vlyt_principal.addLayout(hlyt_fila5)

        # Connects
        self.btn_calcular_caudales.clicked.connect(self.calcular_caudales)
        self.btn_guardar_caudales.clicked.connect(self.guardar_caudales)

    def calcular_caudales(self):
        volumen_widgets = [
            self.lned_volumen1,
            self.lned_volumen2,
            self.lned_volumen3
        ]
        tiempo_widgets = [
            self.lned_tiempo1,
            self.lned_tiempo2,
            self.lned_tiempo3
        ]
        resultado_widgets = [
            self.lbl_resultado1,
            self.lbl_resultado2,
            self.lbl_resultado3
        ]
        ha = self.lned_ha.text()
        decimales = 2

        for index in range(len(volumen_widgets)):
            volumen_widget = volumen_widgets[index]
            tiempo_widget = tiempo_widgets[index]
            resultado_widget = resultado_widgets[index]

            volumen = volumen_widget.text()
            tiempo = tiempo_widget.text()

            if not volumen or not tiempo:
                QMessageBox.warning(self, "Error", "Por favor, complete los campos numéricos.")
                return

            try:
                volumen = float(volumen)
                tiempo = float(tiempo)
                resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
                resultado_widget.setText(f"{resultado:.{decimales}f}")
                volumen_widget.clear()
                tiempo_widget.clear()
            except ValueError:
                QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

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

    def guardar_caudales(self):
        resultado_widgets = [
            self.lbl_resultado1,
            self.lbl_resultado2,
            self.lbl_resultado3,
            self.lbl_resultado4
        ]
        insert_por_aforador = [
            Query.insert_data_afo3_ei,
            Query.insert_data_afo3_tot,
            Query.insert_data_afo3_pp,
            Query.insert_data_parshall
        ]

        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        if not fecha:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha.")
            return

        todos_null = all(widget.text() == "" for widget in resultado_widgets)
        if todos_null:
            respuesta = QMessageBox.question(self, "Advertencia",
                                             "¿Está seguro que desea guardar todos los caudales en nulo?",
                                             QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.No:
                return


        for index, (widget, insert) in enumerate(zip(resultado_widgets, insert_por_aforador), start=1):
            caudal = widget.text()

            if caudal:
                try:
                    caudal = float(caudal)
                    insert(fecha, caudal)
                    widget.clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Error al guardar los datos.")
                except IntegrityError as e:
                    QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")
            else:
                try:
                    insert(fecha, "NULL")
                except IntegrityError as e:
                    QMessageBox.critical(self, "Error",
                                         "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

        QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        self.data_updater.update_data()

    def actualizar_tabla(self):
        self.tabla_embalse_aforadores.update_table()