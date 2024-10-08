from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QColor, QFontDatabase
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit, QComboBox, QGridLayout
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

        #Diccionario de mapeo para insert
        self.insert_functions = {
            "L3-PC1": Query.insert_data_l3_pc1,
            "L3-PC2": Query.insert_data_l3_pc2,
            "L3-PC3": Query.insert_data_l3_pc3,
            "L3-PC4": Query.insert_data_l3_pc4,
            "L3-PC5": Query.insert_data_l3_pc6,
            "L3-PC6": Query.insert_data_l3_pc7
        }

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("PIEZÓMETROS", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha", self)
        lbl_v1 = QLabel("")

        self.lbl_piezometro = QLabel("Piezómetro: ", self)

        self.cmbx_piezometro = QComboBox(self)
        self.cmbx_piezometro.setFixedWidth(150)
        data_tipo = Query.get_piezometros_data()
        if not data_tipo.empty:
            piezometros_list = data_tipo['nombre'].tolist()
            self.cmbx_piezometro.addItems(piezometros_list)

        self.lbl_Np = QLabel("Nivel piezométrico = ")
        self.lbl_resultado = QLabel("")
        self.lbl_resultado.setFixedWidth(150)
        self.lbl_msnm = QLabel("msnm")

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(150)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lbl_lectura = QLabel("Lectura: ")
        self.lned_lectura = QLineEdit(self)
        self.lned_lectura.setFixedWidth(150)

        self.btn_calcular_nps = QPushButton("Calcular", self)
        self.btn_calcular_nps.setObjectName("btn")

        self.btn_guardar_nps = QPushButton("Guardar", self)
        self.btn_guardar_nps.setObjectName("btn")

        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)
        grid_layout.setRowStretch(2, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(5, 1)
        grid_layout.setRowStretch(7, 1)
        grid_layout.setRowStretch(9, 1)
        grid_layout.setRowStretch(11, 1)
        grid_layout.setRowStretch(13, 1)
        grid_layout.setRowStretch(15, 1)
        grid_layout.setRowStretch(16, 1)
        grid_layout.setRowStretch(17, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 4, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 6, 0)
        grid_layout.addWidget(lbl_fecha, 6, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.date_edit, 6, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_piezometro, 8, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmbx_piezometro, 8, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_lectura, 10, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_lectura, 10, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_Np, 12, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_resultado, 12, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_msnm, 12, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_calcular_nps, 14, 1, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_guardar_nps, 14, 2, 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 18, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_calcular_nps.clicked.connect(self.calcular_nps)
        self.btn_guardar_nps.clicked.connect(self.guardar_nps)


    def calcular_nps(self):
        cb_values = [605.22, 604.24, 603.88, 600.60, 616.32, 616.17, 616.02]

        piezometro_index = self.cmbx_piezometro.currentIndex()
        cb = cb_values[piezometro_index]

        lectura = self.lned_lectura.text()
        decimales = 2

        if not lectura:
            QMessageBox.warning(self, "Error", "Por favor, complete el campo numérico.")
            return
        else:
            try:
                lectura = float(lectura)
                resultado = Calculadora.Calculadora().calcular_np(cb, lectura)
                self.lbl_resultado.setText(f"{resultado:.{decimales}f}")
                self.lned_lectura.clear()
            except ValueError:
                QMessageBox.critical(self, "Error", "Valor ingresado no válido. Debe ser un valor numérico.")


    def guardar_nps(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        resultado = self.lbl_resultado.text()
        piezometro = self.cmbx_piezometro.currentText()

        if not fecha:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha.")
            return

        if not resultado:
            respuesta = QMessageBox.question(self, "Advertencia",
                                             "¿Está seguro que desea guardar el nivel piezométrico en nulo?",
                                             QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.No:
                return

        try:
            if resultado:
                resultado = float(resultado)
            else:
                resultado = "NULL"

            insert_function = self.insert_functions[piezometro]
            insert_function(fecha, resultado)
            self.lbl_resultado.clear()
            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
            self.data_updater.update_data()
        except ValueError:
                    QMessageBox.critical(self, "Error", "Error al guardar los datos.")
        except IntegrityError as e:
                    QMessageBox.critical(self, "Error", "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def actualizar_piezometro(self):
        self.lned_lectura.clear()
        self.lbl_resultado.clear()

    def actualizar_tabla(self):
        self.tabla_embalse_7piezometros.update_table()