from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QDateEdit, \
    QTimeEdit, QMessageBox, QGridLayout
from mysql.connector import IntegrityError
from DataBase.Query import Query
from Signals.DataUpdater import DataUpdater


class PrecipitacionView(QWidget):
    def __init__(self, tabla_embalse_precipitacion):
        super(PrecipitacionView,self).__init__()
        self.setup_ui()
        self.tabla_embalse_precipitacion = tabla_embalse_precipitacion
        self.data_updater = DataUpdater()
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("PRECIPITACIONES", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha", self)
        lbl_precipitacion = QLabel("Valor", self)
        lbl_mm = QLabel("mm", self)
        lbl_v1 = QLabel("", self)

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedWidth(170)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_precipitacion = QLineEdit(self)
        self.lned_precipitacion.setFixedWidth(170)

        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.setObjectName("btn")

        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(2, 1)
        grid_layout.setRowStretch(4, 1)
        grid_layout.setRowStretch(6, 1)
        grid_layout.setRowStretch(8, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 3, 0)
        grid_layout.addWidget(lbl_fecha, 3, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.date_edit, 3, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_precipitacion, 5, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_precipitacion, 5, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_mm, 5, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_guardar, 7, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 9, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_guardar.clicked.connect(self.guardar)



    def guardar(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        precipitacion = self.lned_precipitacion.text()

        if not fecha:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha.")
            return
        else:
            try:
                precipitacion = float(precipitacion) if precipitacion else "NULL"

                Query.insert_data_precipitaciones(fecha, precipitacion,)

                self.lned_precipitacion.clear()

                QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
                self.data_updater.update_data()
            except ValueError:
                QMessageBox.critical(self, "Error", "Error al guardar los datos.")
            except IntegrityError as e:
                QMessageBox.critical(self, "Error",
                                         "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def actualizar_tabla(self):
        self.tabla_embalse_precipitacion.update_table()