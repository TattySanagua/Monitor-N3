from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class HomeView(QWidget):
    def __init__(self, tabla_embalse_precipitacion):
        super(HomeView,self).__init__()
        self.setup_ui()

    def setup_ui(self):
        lbl_titulo_ppal = QLabel("PRESA LATERAL N° 3", self)
        lbl_titulo_ppal.setObjectName("title1")

        lbl_txt = QLabel("Software de cálculo de niveles piezométricos, y caudales \n de los instrumentos instalados en presa lateral nº 3 del Cadillal", self)
        lbl_txt.setObjectName("title3")

        vlyt_principal = QVBoxLayout(self)
        vlyt_principal.addWidget(lbl_titulo_ppal, alignment=Qt.AlignCenter)
        vlyt_principal.addWidget(lbl_txt, alignment=Qt.AlignCenter)
