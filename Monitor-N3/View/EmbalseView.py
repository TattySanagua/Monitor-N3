from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDateEdit, \
    QTimeEdit, QMessageBox, QGridLayout
from mysql.connector import IntegrityError
from DataBase.Query import Query
from Signals.DataUpdater import DataUpdater


class EmbalseView(QWidget):
    def __init__(self, tabla_embalse_precipitacion):
        super(EmbalseView,self).__init__()
        self.setup_ui()
        self.tabla_embalse_precipitacion = tabla_embalse_precipitacion
        self.data_updater = DataUpdater()
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("EMBALSE", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha", self)
        lbl_hora = QLabel("Hora", self)
        lbl_nivel_embalse = QLabel("Nivel de embalse", self)
        lbl_m = QLabel("msnm", self)
        lbl_v1 = QLabel("", self)

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.time_edit = QTimeEdit(self)
        self.time_edit.setFixedWidth(160)
        self.time_edit.setDisplayFormat("hh:mm")
        self.time_edit.setTime(QTime.currentTime())

        self.lned_nivel_embalse = QLineEdit(self)
        self.lned_nivel_embalse.setFixedWidth(160)

        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.setObjectName("btn")

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
        grid_layout.setRowStretch(14, 1)
        grid_layout.setRowStretch(15, 1)
        grid_layout.setRowStretch(16, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 4, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 6, 0)
        grid_layout.addWidget(lbl_fecha, 6, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.date_edit, 6, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_hora, 8, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.time_edit, 8, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_nivel_embalse, 10, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_nivel_embalse, 10, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_m, 10, 3, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_guardar, 12, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 17, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_guardar.clicked.connect(self.guardar)

    def guardar(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        hora = self.time_edit.time().toString("hh:mm:ss")
        nivel_embalse = self.lned_nivel_embalse.text()

        if not fecha or not nivel_embalse:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha y/o nivel de embalse.")
            return
        else:
            try:
                nivel_embalse = float(nivel_embalse)
                Query.insert_data_embalse(fecha, hora, nivel_embalse)
                self.lned_nivel_embalse.clear()
                QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
                self.data_updater.update_data()
            except ValueError:
                QMessageBox.critical(self, "Error", "Error al guardar los datos.")
            except IntegrityError as e:
                QMessageBox.critical(self, "Error",
                                         "No se puede agregar el registro.")

    def actualizar_tabla(self):
        self.tabla_embalse_precipitacion.update_table()