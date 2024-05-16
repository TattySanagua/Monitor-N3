from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit
from mysql.connector import IntegrityError
from DataBase.Query import Query
from Signals.DataUpdater import DataUpdater
import Calculadora

class PiezometersView(QWidget):
    def __init__(self, tabla_embalse_7piezometros):
        super(PiezometersView, self).__init__()
        self.setup_ui()
        self.tabla_embalse_7piezometros = tabla_embalse_7piezometros
        self.data_updater = DataUpdater()
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(60)
        lbl_titulo_piezometro = QLabel("Piezómetros", self)

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

        self.btn_calcular_nps = QPushButton("Calcular", self)
        self.btn_calcular_nps.setFixedWidth(120)

        self.btn_guardar_nps = QPushButton("Guardar", self)
        self.btn_guardar_nps.setFixedWidth(120)

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
        hlyt_fila5a = QHBoxLayout()
        hlyt_fila6 = QHBoxLayout()
        hlyt_fila6a = QHBoxLayout()
        hlyt_fila7 = QHBoxLayout()
        hlyt_fila7a = QHBoxLayout()
        hlyt_fila8 = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila1.addWidget(lbl_piezometro1)
        hlyt_fila1.addWidget(self.lned_lectura_p1)
        hlyt_fila1a.addWidget(self.lbl_Np1)
        hlyt_fila1a.addWidget(self.lbl_resultado1)
        hlyt_fila1a.addWidget(self.lbl_msnm1)

        hlyt_fila2.addWidget(lbl_piezometro2)
        hlyt_fila2.addWidget(self.lned_lectura_p2)
        hlyt_fila2a.addWidget(self.lbl_Np2)
        hlyt_fila2a.addWidget(self.lbl_resultado2)
        hlyt_fila2a.addWidget(self.lbl_msnm2)

        hlyt_fila3.addWidget(lbl_piezometro3)
        hlyt_fila3.addWidget(self.lned_lectura_p3)
        hlyt_fila3a.addWidget(self.lbl_Np3)
        hlyt_fila3a.addWidget(self.lbl_resultado3)
        hlyt_fila3a.addWidget(self.lbl_msnm3)

        hlyt_fila4.addWidget(lbl_piezometro4)
        hlyt_fila4.addWidget(self.lned_lectura_p4)
        hlyt_fila4a.addWidget(self.lbl_Np4)
        hlyt_fila4a.addWidget(self.lbl_resultado4)
        hlyt_fila4a.addWidget(self.lbl_msnm4)

        hlyt_fila5.addWidget(lbl_piezometro5)
        hlyt_fila5.addWidget(self.lned_lectura_p5)
        hlyt_fila5a.addWidget(self.lbl_Np5)
        hlyt_fila5a.addWidget(self.lbl_resultado5)
        hlyt_fila5a.addWidget(self.lbl_msnm5)

        hlyt_fila6.addWidget(lbl_piezometro6)
        hlyt_fila6.addWidget(self.lned_lectura_p6)
        hlyt_fila6a.addWidget(self.lbl_Np6)
        hlyt_fila6a.addWidget(self.lbl_resultado6)
        hlyt_fila6a.addWidget(self.lbl_msnm6)

        hlyt_fila7.addWidget(lbl_piezometro7)
        hlyt_fila7.addWidget(self.lned_lectura_p7)
        hlyt_fila7a.addWidget(self.lbl_Np7)
        hlyt_fila7a.addWidget(self.lbl_resultado7)
        hlyt_fila7a.addWidget(self.lbl_msnm7)

        hlyt_fila8.addWidget(self.btn_calcular_nps)
        hlyt_fila8.addWidget(self.btn_guardar_nps)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addWidget(lbl_titulo_piezometro, alignment=Qt.AlignCenter)
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
        vlyt_principal.addLayout(hlyt_fila8)

        self.btn_calcular_nps.clicked.connect(self.calcular_nps)
        self.btn_guardar_nps.clicked.connect(self.guardar_nps)


    def calcular_nps(self):
        cb_values = [605.22, 604.24, 603.88, 600.60, 616.32, 616.17, 616.02]

        lectura_widgets = [
            self.lned_lectura_p1,
            self.lned_lectura_p2,
            self.lned_lectura_p3,
            self.lned_lectura_p4,
            self.lned_lectura_p5,
            self.lned_lectura_p6,
            self.lned_lectura_p7
        ]

        resultado_widgets = [
            self.lbl_resultado1,
            self.lbl_resultado2,
            self.lbl_resultado3,
            self.lbl_resultado4,
            self.lbl_resultado5,
            self.lbl_resultado6,
            self.lbl_resultado7
        ]

        decimales = 2

        for index, cb in enumerate(cb_values):
            lectura_widget = lectura_widgets[index]
            resultado_widget = resultado_widgets[index]

            lectura = lectura_widget.text()

            if not lectura:
                resultado_widget.setText("")
                lectura_widget.clear()
            else:
                try:
                    lectura = float(lectura)
                    resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
                    resultado_widget.setText(f"{resultado:.{decimales}f}")
                    lectura_widget.clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")


    def guardar_nps(self):
        resultado_widgets = [
            self.lbl_resultado1,
            self.lbl_resultado2,
            self.lbl_resultado3,
            self.lbl_resultado4,
            self.lbl_resultado5,
            self.lbl_resultado6,
            self.lbl_resultado7
        ]

        insert_por_piezometro = [
            Query.insert_data_l3_pc1,
            Query.insert_data_l3_pc2,
            Query.insert_data_l3_pc3,
            Query.insert_data_l3_pc4,
            Query.insert_data_l3_pc5,
            Query.insert_data_l3_pc6,
            Query.insert_data_l3_pc7
        ]

        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        if not fecha:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha.")
            return

        todos_null = all(widget.text() == "" for widget in resultado_widgets)
        if todos_null:
            respuesta = QMessageBox.question(self, "Advertencia",
                                             "¿Está seguro que desea guardar todos los niveles piezométricos en nulo?",
                                             QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.No:
                return

        for index, (widget, insert) in enumerate(zip(resultado_widgets, insert_por_piezometro), start=1):
            nivel_piezometrico = widget.text()

            if nivel_piezometrico:
                try:
                    nivel_piezometrico = float(nivel_piezometrico)
                    insert(fecha, nivel_piezometrico)
                    widget.clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Error al guardar los datos.")
                except IntegrityError as e:
                    QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")
            else:
                try:
                    insert(fecha, "NULL")
                except IntegrityError as e:
                    QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

        QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
        self.data_updater.update_data()


    def actualizar_tabla(self):
        self.tabla_embalse_7piezometros.update_table()