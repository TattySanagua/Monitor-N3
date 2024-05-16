from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QDateEdit, \
    QTimeEdit, QMessageBox
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

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_fecha.setFixedWidth(110)
        lbl_precipitacion = QLabel("Precipitación", self)
        lbl_precipitacion.setFixedWidth(110)
        lbl_tres = QLabel("Tres días previos", self)
        lbl_tres.setFixedWidth(110)
        lbl_cinco = QLabel("Cinco días previos", self)
        lbl_cinco.setFixedWidth(110)
        lbl_diez = QLabel("Diez días previos", self)
        lbl_diez.setFixedWidth(110)

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedWidth(160)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_precipitacion = QLineEdit(self)
        self.lned_precipitacion.setFixedWidth(160)

        self.lned_tres_dias_previos = QLineEdit(self)
        self.lned_tres_dias_previos.setFixedWidth(160)

        self.lned_cinco_dias_previos = QLineEdit(self)
        self.lned_cinco_dias_previos.setFixedWidth(160)

        self.lned_diez_dias_previos = QLineEdit(self)
        self.lned_diez_dias_previos.setFixedWidth(160)

        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.setFixedWidth(130)

        hlyt_fecha = QHBoxLayout()
        hlyt_fecha.addWidget(lbl_fecha, alignment=Qt.AlignCenter)
        hlyt_fecha.addWidget(self.date_edit, alignment=Qt.AlignCenter)

        hlyt_precipitacion = QHBoxLayout()
        hlyt_precipitacion.addWidget(lbl_precipitacion)
        hlyt_precipitacion.addWidget(self.lned_precipitacion)

        hlyt_tres = QHBoxLayout()
        hlyt_tres.addWidget(lbl_tres)
        hlyt_tres.addWidget(self.lned_tres_dias_previos)

        hlyt_cinco = QHBoxLayout()
        hlyt_cinco.addWidget(lbl_cinco)
        hlyt_cinco.addWidget(self.lned_cinco_dias_previos)

        hlyt_diez = QHBoxLayout()
        hlyt_diez.addWidget(lbl_diez)
        hlyt_diez.addWidget(self.lned_diez_dias_previos)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)

        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_precipitacion)
        vlyt_principal.addLayout(hlyt_tres)
        vlyt_principal.addLayout(hlyt_cinco)
        vlyt_principal.addLayout(hlyt_diez)
        vlyt_principal.addWidget(self.btn_guardar, alignment=Qt.AlignCenter)

        self.btn_guardar.clicked.connect(self.guardar)

    def guardar(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")
        precipitacion = self.lned_precipitacion.text()
        tres = self.lned_tres_dias_previos.text()
        cinco = self.lned_cinco_dias_previos.text()
        diez = self.lned_diez_dias_previos.text()

        if not fecha:
            QMessageBox.warning(self, "Error", "Debe ingresar una fecha.")
            return
        else:
            try:
                precipitacion = float(precipitacion) if precipitacion else "NULL"
                tres = float(tres) if tres else "NULL"
                cinco = float(cinco) if cinco else "NULL"
                diez = float(diez) if diez else "NULL"

                Query.insert_data_precipitaciones(fecha, precipitacion, tres, cinco, diez)

                self.lned_precipitacion.clear()
                self.lned_tres_dias_previos.clear()
                self.lned_cinco_dias_previos.clear()
                self.lned_diez_dias_previos.clear()

                QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
                self.data_updater.update_data()
            except ValueError:
                QMessageBox.critical(self, "Error", "Error al guardar los datos.")
            except IntegrityError as e:
                QMessageBox.critical(self, "Error",
                                         "No se puede agregar el registro, no existe nivel de embalse para la fecha ingresada.")

    def actualizar_tabla(self):
        self.tabla_embalse_precipitacion.update_table()