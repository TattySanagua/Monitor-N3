from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class HomeView(QWidget):
    def __init__(self):
        super(HomeView,self).__init__()
        self.setup_ui()

    def setup_ui(self):

        lbl_titulo_ppal = QLabel("Presa Lateral N° 3", self)
        lbl_fecha = QLabel("Fecha", self)
        lbl_nivel_embalse = QLabel("Nivel de embalse", self)

        self.datetime_edit = QDateTimeEdit(self)
        self.datetime_edit.setCalendarPopup(True)
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())

        self.lned_nivel_embalse = QLineEdit(self)

        self.btn_guardar = QPushButton("Guardar", self)

        hlyt_fecha = QHBoxLayout()
        hlyt_fecha.addWidget(lbl_fecha)
        hlyt_fecha.addWidget(self.datetime_edit)

        hlyt_embalse = QHBoxLayout()
        hlyt_embalse.addWidget(lbl_nivel_embalse)
        hlyt_embalse.addWidget(self.lned_nivel_embalse)

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.setAlignment(Qt.AlignVCenter)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addLayout(hlyt_fecha)
        vlyt_principal.addLayout(hlyt_embalse)
        vlyt_principal.addWidget(self.btn_guardar)