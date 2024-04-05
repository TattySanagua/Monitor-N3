from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QDateEdit, \
    QTimeEdit


class HomeView(QWidget):
    def __init__(self):
        super(HomeView,self).__init__()
        self.setup_ui()

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_hora = QLabel("Hora", self)
        lbl_nivel_embalse = QLabel("Nivel de embalse", self)
        lbl_m = QLabel("msnm", self)

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedWidth(130)
        self.date_edit.setDate(QDate.currentDate())

        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("hh:mm")
        self.time_edit.setFixedWidth(130)
        self.time_edit.setTime(QTime.currentTime())

        self.lned_nivel_embalse = QLineEdit(self)
        self.lned_nivel_embalse.setFixedWidth(200)

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
        hlyt_embalse.addWidget(lbl_m)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)

        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_hora)
        vlyt_principal.addLayout(hlyt_embalse)
        vlyt_principal.addWidget(self.btn_guardar, alignment=Qt.AlignCenter)