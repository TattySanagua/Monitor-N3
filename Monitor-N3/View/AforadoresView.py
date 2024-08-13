from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit, QGridLayout, QComboBox
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

        self.insert_functions = {
            "AFo3-EI": Query.insert_data_afo3_ei,
            "AFo3-PP": Query.insert_data_afo3_pp
        }

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("AFORADORES", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha", self)
        lbl_aforadores = QLabel("Aforadores volumétricos", self)
        lbl_aforadores.setObjectName("title3")

        lbl_lectura_1 = QLabel("Lectura 1")
        lbl_lectura_2 = QLabel("Lectura 2")
        lbl_lectura_3 = QLabel("Lectura 3")

        self.cmbox_aforadores = QComboBox(self)
        self.cmbox_aforadores.setFixedWidth(150)
        self.cmbox_aforadores.addItems(["AFo3-EI", "AFo3-PP"])
        self.cmbox_aforadores.currentIndexChanged.connect(self.actualizar_aforador)

        lbl_parshall = QLabel("AFo3-TOT/Parshall", self)
        lbl_parshall.setObjectName("title3")
        lbl_formula_parshall = QLabel("Caudal Q [m3/seg] = K*ha^u", self)
        lbl_descripcion1 = QLabel("Para ancho de garganta de 3 pulgadas, K = 0.1771 y u = 1.55", self)
        lbl_descripcion2 = QLabel("ha: Tirante medido en la zona de convergencia [m]", self)
        lbl_ha = QLabel("ha", self)
        lbl_v1 = QLabel(" ")
        lbl_v2 = QLabel(" ")

        self.lbl_caudal_1 = QLabel("Q = ") #Result 1
        self.lbl_resultado_1 = QLabel("")
        self.lbl_ls_1 = QLabel("l/s")
        self.lbl_caudal_2 = QLabel("Q = ") #Result 2
        self.lbl_resultado_2 = QLabel("")
        self.lbl_ls_2 = QLabel("l/s")
        self.lbl_caudal_3 = QLabel("Q = ") #Result 3
        self.lbl_resultado_3 = QLabel("")
        self.lbl_ls_3 = QLabel("l/s")
        self.lbl_caudal_promedio = QLabel("Qpromedio = ")  # Promedio
        self.lbl_resultado_promedio = QLabel("")
        self.lbl_ls_promedio = QLabel("l/s")

        self.lbl_caudal_parshall = QLabel("Q = ")
        self.lbl_resultado_parshall = QLabel("")
        self.lbl_m3s = QLabel("m3/s")

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(150)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_volumen_1 = QLineEdit(self)
        self.lned_volumen_1.setPlaceholderText("Volumen l")
        self.lned_volumen_2 = QLineEdit(self)
        self.lned_volumen_2.setPlaceholderText("Volumen l")
        self.lned_volumen_3 = QLineEdit(self)
        self.lned_volumen_3.setPlaceholderText("Volumen l")
        self.lned_tiempo_1 = QLineEdit(self)
        self.lned_tiempo_1.setPlaceholderText("Tiempo s")
        self.lned_tiempo_2 = QLineEdit(self)
        self.lned_tiempo_2.setPlaceholderText("Tiempo s")
        self.lned_tiempo_3 = QLineEdit(self)
        self.lned_tiempo_3.setPlaceholderText("Tiempo s")

        self.lned_ha = QLineEdit(self)

        self.btn_calcular_caudales = QPushButton("Calcular", self)
        self.btn_calcular_caudales.setObjectName("btn")
        self.btn_guardar_caudales = QPushButton("Guardar", self)
        self.btn_guardar_caudales.setObjectName("btn")
        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(1, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(5, 1)
        grid_layout.setRowStretch(10, 1)
        grid_layout.setRowStretch(15, 1)
        grid_layout.setRowStretch(17, 1)
        grid_layout.setRowStretch(19, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 0, 2, 1, 3, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_fecha, 2, 2, alignment=Qt.AlignRight)
        grid_layout.addWidget(self.date_edit, 2, 3, 1, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_aforadores, 4, 1, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmbox_aforadores, 4, 3, 1, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v1, 6, 0)
        grid_layout.addWidget(lbl_lectura_1, 6, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_1, 6, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_1, 6, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_1, 6, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_1, 6, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_1, 6, 6, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v2, 6, 7)
        grid_layout.addWidget(lbl_lectura_2, 7, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_2, 7, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_2, 7, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_2, 7, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_2, 7, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_2, 7, 6, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_lectura_3, 8, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_3, 8, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_3, 8, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_3, 8, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_3, 8, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_3, 8, 6, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_promedio, 9, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_promedio, 9, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_promedio, 9, 6, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_parshall, 11, 1, 1, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_formula_parshall, 12, 1, 1, 3,  alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_descripcion1, 13, 1, 1, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_descripcion2, 14, 1, 1, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_ha, 16, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_ha, 16, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_parshall, 16, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_parshall, 16, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_m3s, 16, 6, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_calcular_caudales, 18, 2, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_guardar_caudales, 18, 4, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 20, 2, 1, 3, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        # Connects
        self.btn_calcular_caudales.clicked.connect(self.calcular_caudales)
        self.btn_guardar_caudales.clicked.connect(self.guardar_caudales)

    def calcular_caudales(self):
        volumen_widgets = [
            self.lned_volumen_1,
            self.lned_volumen_2,
            self.lned_volumen_3
        ]
        tiempo_widgets = [
            self.lned_tiempo_1,
            self.lned_tiempo_2,
            self.lned_tiempo_3
        ]
        resultado_widgets = [
            self.lbl_resultado_1,
            self.lbl_resultado_2,
            self.lbl_resultado_3
        ]

        ha = self.lned_ha.text()
        decimales = 2
        caudales = []

        for index in range(len(volumen_widgets)):
            volumen = volumen_widgets[index].text()
            tiempo = tiempo_widgets[index].text()
            resultado_widget = resultado_widgets[index]

            if volumen and tiempo:
                try:
                    volumen = float(volumen)
                    tiempo = float(tiempo)
                    resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
                    caudales.append(resultado)
                    resultado_widget.setText(f"{resultado:.{decimales}f}")
                    volumen_widgets[index].clear()
                    tiempo_widgets[index].clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

        if caudales:
            promedio = sum(caudales)/len(caudales)
            self.lbl_resultado_promedio.setText(f"{promedio:.{decimales}f}")

        if ha:
            try:
                ha = float(ha)
                resultado = Calculadora.Calculadora().calcular_caudal_parshall(ha)
                self.lbl_resultado_parshall.setText(f"{resultado:.{decimales}f}")
                self.lned_ha.clear()
            except ValueError:
                QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def guardar_caudales(self):
        aforador_seleccionado = self.cmbox_aforadores.currentText()

        if aforador_seleccionado not in self.insert_functions:
            QMessageBox.warning(self, "Error", "Aforador no reconocido, seleccione uno.")
            return

        insert_func = self.insert_functions.get(aforador_seleccionado)

        resultado_widgets = [
            self.lbl_resultado_promedio,
            self.lbl_resultado_parshall,
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

        # Guardar datos del aforador volumétrico seleccionado desde el ComboBox
        if aforador_seleccionado in self.insert_functions:
            widget_volumetrico = self.lbl_resultado_promedio
            caudal = widget_volumetrico.text()

            if caudal:
                try:
                    caudal = float(caudal)
                    insert_func(fecha, caudal)
                    widget_volumetrico.clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Error al guardar los datos.")
                except IntegrityError as e:
                    QMessageBox.critical(self, "Error",
                                         "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")
            else:
                try:
                    insert_func(fecha, "NULL")
                except IntegrityError as e:
                    QMessageBox.critical(self, "Error",
                                         "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

        # Guardar datos del aforador Parshall
        widget_parshall = self.lbl_resultado_parshall
        caudal_parshall = widget_parshall.text()

        if caudal_parshall:
            try:
                caudal_parshall = float(caudal_parshall)
                Query.insert_data_afo3_tot(fecha, caudal_parshall)
                widget_parshall.clear()
            except ValueError:
                QMessageBox.critical(self, "Error", "Error al guardar los datos del aforador Parshall.")
            except IntegrityError as e:
                QMessageBox.critical(self, "Error",
                                     "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

        self.lned_volumen_1.clear()
        self.lned_volumen_2.clear()
        self.lned_volumen_3.clear()
        self.lned_tiempo_1.clear()
        self.lned_tiempo_2.clear()
        self.lned_tiempo_3.clear()
        self.lbl_resultado_1.clear()
        self.lbl_resultado_2.clear()
        self.lbl_resultado_3.clear()
        self.lbl_resultado_promedio.clear()
        self.lned_ha.clear()
        self.lbl_resultado_parshall.clear()

        QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        self.data_updater.update_data()

    def actualizar_aforador(self):
        self.lned_volumen_1.clear()
        self.lned_volumen_2.clear()
        self.lned_volumen_3.clear()
        self.lned_tiempo_1.clear()
        self.lned_tiempo_2.clear()
        self.lned_tiempo_3.clear()
        self.lbl_resultado_1.clear()
        self.lbl_resultado_2.clear()
        self.lbl_resultado_3.clear()
        self.lbl_resultado_promedio.clear()

    def actualizar_tabla(self):
        self.tabla_embalse_aforadores.update_table()