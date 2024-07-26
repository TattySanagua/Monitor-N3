from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap


class HomeView(QWidget):
    def __init__(self, tabla_embalse_precipitacion):
        super(HomeView,self).__init__()
        self.setup_ui()

    def setup_ui(self):
        lbl_titulo_ppal = QLabel("PRESA LATERAL N° 3", self)
        lbl_titulo_ppal.setObjectName("title1")
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")

        lbl_txt = QLabel("Software de cálculo de niveles piezométricos, caudales e informes gráficos de los instrumentos instalados en Presa Lateral Nº 3 del Cadillal", self)
        lbl_txt.setObjectName("title3")
        lbl_txt.setWordWrap(True)

        lbl_img = QLabel(self)
        pixmap = QPixmap("../LogoOrsep_sin_fondo.png")
        lbl_img.setPixmap(pixmap)
        lbl_img.setAlignment(Qt.AlignCenter)

        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout()

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(2, 1)
        grid_layout.setRowStretch(6, 1)
        grid_layout.setRowStretch(9, 1)

        grid_layout.addWidget(lbl_v1, 1, 0)
        grid_layout.addWidget(lbl_titulo_ppal, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v2, 1, 3)
        grid_layout.addWidget(lbl_txt, 3, 1, 3, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_img, 7, 1, 2, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 10, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)