import math

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QDateEdit, QLineEdit, QComboBox, \
    QPushButton, QGridLayout, QWidget
from DataBase.Query import Query

class FormInstrumentsView(QWidget):
    def __init__(self):
        super(FormInstrumentsView,self).__init__()
        self.setWindowTitle("Agregar Instrumento")
        self.setGeometry(300, 130, 300, 300)
        self.setup_ui()

    def setup_ui(self):
        lbl_titulo_ppal = QLabel("Formulario de instrumento", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_fecha = QLabel("Fecha instalación", self)
        lbl_nombre = QLabel("Nombre", self)
        lbl_tipo = QLabel("Tipo", self)
        lbl_v1 = QLabel(" ", self)
        lbl_v2 = QLabel(" ", self)

        self.date_edit = QDateEdit(self)
        self.date_edit.setFixedWidth(180)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.lned_nombre = QLineEdit(self)
        self.lned_nombre.setFixedWidth(180)

        self.cmb_tipe = QComboBox(self)
        self.cmb_tipe.setFixedWidth(180)
        self.cmb_tipe.addItems(["PIEZOMETRO", "FREATIMETRO", "AFORADOR VOLUMETRICO", "AFORADOR PARSHALL"])

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
        grid_layout.setRowStretch(10, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 1, 1, 1, 3, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 3, 0)
        grid_layout.addWidget(lbl_nombre, 3, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_nombre, 3, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v2, 3, 4)
        grid_layout.addWidget(lbl_tipo, 5, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmb_tipe, 5, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_fecha, 7, 1, 1, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.date_edit, 7, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_guardar, 9, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(footer_label, 11, 1, 1, 3, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_guardar.clicked.connect(self.guardar)

    def guardar(self):
        fecha = self.date_edit.date().toString("yyyy-MM-dd")

        nivel_embalse = self.lned_nivel_embalse.text()