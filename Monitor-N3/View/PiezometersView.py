from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QColor, QFontDatabase
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMessageBox, QDateEdit, QComboBox
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
        self.setStyleSheet("""
                    QWidget {
                        background-color: #F0F0F0;
                    }
                    QLabel {
                        color: #333333;
                    }
                    QLineEdit, QDateEdit, QComboBox {
                        border: 1px solid #CCCCCC;
                        padding: 5px;
                        color: #333333;
                        background-color: #FFFFFF;
                    }
                    QPushButton {
                        background-color: #4A90E2;
                        color: #FFFFFF;
                        border: none;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: #0056b3;
                    }
                    QMessageBox {
                        background-color: #F0F0F0;
                        color: #333333;
                    }
                """)
        lbl_titulo_ppal = QLabel("PIEZÓMETROS", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(60)

        self.lbl_piezometro = QLabel("Piezómetro: ", self)
        self.lbl_piezometro.setFixedWidth(80)

        self.cmbx_piezometro = QComboBox(self)
        self.cmbx_piezometro.addItems(["L3-PC1", "L3-PC2", "L3-PC3", "L3-PC4", "L3-PC5", "L3-PC6", "L3-PC7"])
        self.cmbx_piezometro.currentIndexChanged.connect(self.actualizar_piezometro)

        self.lbl_Np = QLabel("Np = ")
        self.lbl_Np.setFixedWidth(60)
        self.lbl_resultado = QLabel("")
        self.lbl_resultado.setFixedWidth(100)
        self.lbl_msnm = QLabel("msnm")
        self.lbl_msnm.setFixedWidth(55)

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lbl_lectura = QLabel("Lectura: ")
        self.lbl_lectura.setFixedWidth(60)
        self.lned_lectura = QLineEdit(self)
        self.lned_lectura.setFixedWidth(160)


        self.btn_calcular_nps = QPushButton("Calcular", self)
        self.btn_calcular_nps.setFixedWidth(120)

        self.btn_guardar_nps = QPushButton("Guardar", self)
        self.btn_guardar_nps.setFixedWidth(120)

        hlyt_fecha = QHBoxLayout()
        hlyt_fila_cmbx = QHBoxLayout()
        hlyt_fila_lectura = QHBoxLayout()
        hlyt_fila_resultado = QHBoxLayout()
        hlyt_fila_btns = QHBoxLayout()

        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.date_edit)

        hlyt_fila_cmbx.addWidget(self.lbl_piezometro)
        hlyt_fila_cmbx.addWidget(self.cmbx_piezometro)

        hlyt_fila_lectura.addWidget(self.lbl_lectura)
        hlyt_fila_lectura.addWidget(self.lned_lectura)

        hlyt_fila_resultado.addWidget(self.lbl_Np)
        hlyt_fila_resultado.addWidget(self.lbl_resultado)
        hlyt_fila_resultado.addWidget(self.lbl_msnm)

        hlyt_fila_btns.addWidget(self.btn_calcular_nps)
        hlyt_fila_btns.addWidget(self.btn_guardar_nps)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_fila_cmbx)
        vlyt_principal.addLayout(hlyt_fila_lectura)
        vlyt_principal.addLayout(hlyt_fila_resultado)
        vlyt_principal.addLayout(hlyt_fila_btns)

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