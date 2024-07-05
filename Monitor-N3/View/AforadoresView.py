from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit, QGridLayout
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

        lbl_titulo_ppal = QLabel("AFORADORES", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha", self)

        #Volumétricos: EI and PP
        lbl_titulo_aforadores = QLabel("Aforadores volumétricos", self)
        lbl_titulo_aforadores.setObjectName("title3")
        lbl_afo3_ei = QLabel("AFo3-EI:", self)
        lbl_lectura_vol_ei_1 = QLabel("Lectura 1")
        lbl_lectura_vol_ei_2 = QLabel("Lectura 2")
        lbl_lectura_vol_ei_3 = QLabel("Lectura 3")

        lbl_afo3_pp = QLabel("AFo3-PP:", self)
        lbl_lectura_vol_pp_1 = QLabel("Lectura 1")
        lbl_lectura_vol_pp_2 = QLabel("Lectura 2")
        lbl_lectura_vol_pp_3 = QLabel("Lectura 3")

        lbl_titulo_parshall = QLabel("AFo3-TOT/Parshall", self)
        lbl_titulo_parshall.setObjectName("title3")
        lbl_formula_parshall = QLabel("Caudal Q [m3/seg] = K*ha^u", self)
        lbl_descripcion1 = QLabel("Para ancho de garganta de 3 pulgadas, K = 0.1771 y u = 1.55", self)
        lbl_descripcion2 = QLabel("ha: Tirante medido en la zona de convergencia [m]", self)
        lbl_ha = QLabel("ha", self)
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")
        #EI
        self.lbl_caudal_ei_1 = QLabel("Q = ") #Result 1 ei
        self.lbl_resultado_ei_1 = QLabel("")
        self.lbl_ls_ei_1 = QLabel("l/s")
        self.lbl_caudal_ei_2 = QLabel("Q = ") #Result 2 ei
        self.lbl_resultado_ei_2 = QLabel("")
        self.lbl_ls_ei_2 = QLabel("l/s")
        self.lbl_caudal_ei_3 = QLabel("Q = ") #Result 3 ei
        self.lbl_resultado_ei_3 = QLabel("")
        self.lbl_ls_ei_3 = QLabel("l/s")
        self.lbl_caudal_ei_promedio = QLabel("Qpromedio = ")  # Promedio ei
        self.lbl_resultado_ei_promedio = QLabel("")
        self.lbl_ls_ei_promedio = QLabel("l/s")
        #PP
        self.lbl_caudal_pp_1 = QLabel("Q = ") #Result 1 pp
        self.lbl_resultado_pp_1 = QLabel("")
        self.lbl_ls_pp_1 = QLabel("l/s")
        self.lbl_caudal_pp_2 = QLabel("Q = ")  # Result 2 pp
        self.lbl_resultado_pp_2 = QLabel("")
        self.lbl_ls_pp_2 = QLabel("l/s")
        self.lbl_caudal_pp_3 = QLabel("Q = ")  # Result 3 pp
        self.lbl_resultado_pp_3 = QLabel("")
        self.lbl_ls_pp_3 = QLabel("l/s")
        self.lbl_caudal_pp_promedio = QLabel("Qpromedio = ")  # Promedio pp
        self.lbl_resultado_pp_promedio = QLabel("")
        self.lbl_ls_pp_promedio = QLabel("l/s")
        #
        self.lbl_caudal_parshall = QLabel("Q = ")
        self.lbl_resultado_parshall = QLabel("")
        self.lbl_m3s = QLabel("m3/s")

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_volumen_ei_1 = QLineEdit(self)
        self.lned_volumen_ei_1.setPlaceholderText("Volumen l")
        self.lned_volumen_ei_2 = QLineEdit(self)
        self.lned_volumen_ei_2.setPlaceholderText("Volumen l")
        self.lned_volumen_ei_3 = QLineEdit(self)
        self.lned_volumen_ei_3.setPlaceholderText("Volumen l")
        self.lned_tiempo_ei_1 = QLineEdit(self)
        self.lned_tiempo_ei_1.setPlaceholderText("Tiempo s")
        self.lned_tiempo_ei_2 = QLineEdit(self)
        self.lned_tiempo_ei_2.setPlaceholderText("Tiempo s")
        self.lned_tiempo_ei_3 = QLineEdit(self)
        self.lned_tiempo_ei_3.setPlaceholderText("Tiempo s")

        self.lned_volumen_pp_1 = QLineEdit(self)
        self.lned_volumen_pp_1.setPlaceholderText("Volumen l")
        self.lned_volumen_pp_2 = QLineEdit(self)
        self.lned_volumen_pp_2.setPlaceholderText("Volumen l")
        self.lned_volumen_pp_3 = QLineEdit(self)
        self.lned_volumen_pp_3.setPlaceholderText("Volumen l")
        self.lned_tiempo_pp_1 = QLineEdit(self)
        self.lned_tiempo_pp_1.setPlaceholderText("Tiempo s")
        self.lned_tiempo_pp_2 = QLineEdit(self)
        self.lned_tiempo_pp_2.setPlaceholderText("Tiempo s")
        self.lned_tiempo_pp_3 = QLineEdit(self)
        self.lned_tiempo_pp_3.setPlaceholderText("Tiempo s")

        self.lned_ha = QLineEdit(self)

        self.btn_calcular_caudales = QPushButton("Calcular", self)
        self.btn_calcular_caudales.setObjectName("btn")
        self.btn_guardar_caudales = QPushButton("Guardar", self)
        self.btn_guardar_caudales.setObjectName("btn")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(10, 1)
        grid_layout.setRowStretch(16, 1)
        grid_layout.setRowStretch(22, 1)
        grid_layout.setRowStretch(24, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 1, 2, 1, 3, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_fecha, 2, 2, alignment=Qt.AlignRight)
        grid_layout.addWidget(self.date_edit, 2, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v1, 4, 0)
        grid_layout.addWidget(lbl_titulo_aforadores, 4, 1, 1, 3, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_afo3_ei, 5, 1, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_lectura_vol_ei_1, 6, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_ei_1, 6, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_ei_1, 6, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_ei_1, 6, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_ei_1, 6, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_ei_1, 6, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_lectura_vol_ei_2, 7, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_ei_2, 7, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_ei_2, 7, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_ei_2, 7, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_ei_2, 7, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_ei_2, 7, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_lectura_vol_ei_3, 8, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_ei_3, 8, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_ei_3, 8, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_ei_3, 8, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_ei_3, 8, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_ei_3, 8, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(self.lbl_caudal_ei_promedio, 9, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_ei_promedio, 9, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_ei_promedio, 9, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_afo3_pp, 11, 1, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_lectura_vol_pp_1, 12, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_pp_1, 12, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_pp_1, 12, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_pp_1, 12, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_pp_1, 12, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_pp_1, 12, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_lectura_vol_pp_2, 13, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_pp_2, 13, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_pp_2, 13, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_pp_2, 13, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_pp_2, 13, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_pp_2, 13, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_lectura_vol_pp_3, 14, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_volumen_pp_3, 14, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_tiempo_pp_3, 14, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_pp_3, 14, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_pp_3, 14, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_pp_3, 14, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(self.lbl_caudal_pp_promedio, 15, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_pp_promedio, 15, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_ls_pp_promedio, 15, 6, alignment=Qt.AlignLeft)

        grid_layout.addWidget(lbl_titulo_parshall, 17, 1, 1, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_formula_parshall, 18, 1, 1, 3,  alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_descripcion1, 19, 1, 1, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_descripcion2, 20, 1, 1, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_ha, 21, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_ha, 21, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_caudal_parshall, 21, 4, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado_parshall, 21, 5, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_m3s, 21, 6, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v2, 21, 7)

        grid_layout.addWidget(self.btn_calcular_caudales, 24, 2, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_guardar_caudales, 24, 4, 1, 1, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        # Connects
        self.btn_calcular_caudales.clicked.connect(self.calcular_caudales)
        self.btn_guardar_caudales.clicked.connect(self.guardar_caudales)

    def calcular_caudales(self):
        volumen_ei_widgets = [
            self.lned_volumen_ei_1,
            self.lned_volumen_ei_2,
            self.lned_volumen_ei_3
        ]
        tiempo_ei_widgets = [
            self.lned_tiempo_ei_1,
            self.lned_tiempo_ei_2,
            self.lned_tiempo_ei_3
        ]
        resultado_ei_widgets = [
            self.lbl_resultado_ei_1,
            self.lbl_resultado_ei_2,
            self.lbl_resultado_ei_3
        ]
        volumen_pp_widgets = [
            self.lned_volumen_pp_1,
            self.lned_volumen_pp_2,
            self.lned_volumen_pp_3
        ]

        tiempo_pp_widgets = [
            self.lned_tiempo_pp_1,
            self.lned_tiempo_pp_2,
            self.lned_tiempo_pp_3
        ]

        resultado_pp_widgets = [
            self.lbl_resultado_pp_1,
            self.lbl_resultado_pp_2,
            self.lbl_resultado_pp_3
        ]
        ha = self.lned_ha.text()
        decimales = 2
        caudales_ei = []
        caudales_pp = []

        for index in range(len(volumen_ei_widgets)):
            volumen = volumen_ei_widgets[index].text()
            tiempo = tiempo_ei_widgets[index].text()
            resultado_ei_widget = resultado_ei_widgets[index]

            if volumen and tiempo:
                try:
                    volumen = float(volumen)
                    tiempo = float(tiempo)
                    resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
                    caudales_ei.append(resultado)
                    resultado_ei_widget.setText(f"{resultado:.{decimales}f}")
                    volumen_ei_widgets[index].clear()
                    tiempo_ei_widgets[index].clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

        if caudales_ei:
            promedio_ei = sum(caudales_ei)/len(caudales_ei)
            self.lbl_resultado_ei_promedio.setText(f"{promedio_ei:.{decimales}f}")

        for index in range(len(volumen_pp_widgets)):
            volumen = volumen_pp_widgets[index].text()
            tiempo = tiempo_pp_widgets[index].text()
            resultado_pp_widget = resultado_pp_widgets[index]

            if volumen and tiempo:
                try:
                    volumen = float(volumen)
                    tiempo = float(tiempo)
                    resultado = Calculadora.Calculadora().calcular_caudal(volumen, tiempo)
                    caudales_pp.append(resultado)
                    resultado_pp_widget.setText(f"{resultado:.{decimales}f}")
                    volumen_pp_widgets[index].clear()
                    tiempo_pp_widgets[index].clear()
                except ValueError:
                    QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

        if caudales_pp:
            promedio_pp = sum(caudales_pp)/len(caudales_pp)
            self.lbl_resultado_pp_promedio.setText(f"{promedio_pp:.{decimales}f}")

        if ha:
            try:
                ha = float(ha)
                resultado = Calculadora.Calculadora().calcular_caudal_parshall(ha)
                self.lbl_resultado_parshall.setText(f"{resultado:.{decimales}f}")
                self.lned_ha.clear()
            except ValueError:
                QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")

    def guardar_caudales(self):
        resultado_widgets = [
            self.lbl_resultado_ei_promedio,
            self.lbl_resultado_parshall,
            self.lbl_resultado_pp_promedio
        ]
        insert_por_aforador = [
            Query.insert_data_afo3_ei,
            Query.insert_data_afo3_tot,
            Query.insert_data_afo3_pp
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

        self.lbl_caudal_ei_1.clear()
        self.lbl_caudal_ei_2.clear()
        self.lbl_caudal_ei_3.clear()
        self.lbl_caudal_pp_1.clear()
        self.lbl_caudal_pp_2.clear()
        self.lbl_caudal_pp_3.clear()

        QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.", QMessageBox.Ok)
        self.data_updater.update_data()

    def actualizar_tabla(self):
        self.tabla_embalse_aforadores.update_table()