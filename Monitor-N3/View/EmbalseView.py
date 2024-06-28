from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QDateEdit, \
    QTimeEdit, QMessageBox
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

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(110)
        lbl_hora = QLabel("Hora", self)
        lbl_hora.setFixedWidth(110)
        lbl_nivel_embalse = QLabel("Nivel de embalse", self)
        lbl_nivel_embalse.setFixedWidth(110)
        lbl_m = QLabel("msnm", self)

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setDate(QDate.currentDate())

        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("hh:mm")
        self.time_edit.setFixedWidth(160)
        self.time_edit.setTime(QTime.currentTime())

        self.lned_nivel_embalse = QLineEdit(self)
        self.lned_nivel_embalse.setFixedWidth(160)

        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.setFixedWidth(130)

        hlyt_fecha = QHBoxLayout()
        hlyt_fecha.addWidget(lbl_fecha, alignment=Qt.AlignCenter)
        hlyt_fecha.addWidget(self.date_edit, alignment=Qt.AlignCenter)

        hlyt_hora = QHBoxLayout()
        hlyt_hora.addWidget(lbl_hora, alignment=Qt.AlignCenter)
        hlyt_hora.addWidget(self.time_edit, alignment=Qt.AlignCenter)

        hlyt_embalse = QHBoxLayout()
        hlyt_embalse.addWidget(lbl_nivel_embalse, alignment=Qt.AlignCenter)
        hlyt_embalse.addWidget(self.lned_nivel_embalse, alignment=Qt.AlignCenter)
        hlyt_embalse.addWidget(lbl_m, alignment=Qt.AlignCenter)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)

        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_hora)
        vlyt_principal.addLayout(hlyt_embalse)
        vlyt_principal.addWidget(self.btn_guardar, alignment=Qt.AlignCenter)

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