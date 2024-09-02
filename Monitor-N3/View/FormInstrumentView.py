import math

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QDateEdit, QLineEdit, QComboBox, \
    QPushButton, QGridLayout, QWidget, QMessageBox
from DataBase.Query import Query
from Signals.DataUpdater import DataUpdater

class FormInstrumentsView(QWidget):
    def __init__(self, tabla_instrumentos):
        super(FormInstrumentsView,self).__init__()
        self.setup_ui()
        self.tabla_instrumentos = tabla_instrumentos
        self.data_updater = DataUpdater()
        self.data_updater.data_updated_signal.connect(self.actualizar_tabla)

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
        data_tipo = Query.get_tipo()
        if not data_tipo.empty:
            tipos_list = data_tipo['Tipo'].tolist()
            self.cmb_tipe.addItems(tipos_list)

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
        nombre = self.lned_nombre.text().strip()
        tipo_nombre = self.cmb_tipe.currentText().strip()
        fecha = self.date_edit.date().toString("yyyy-MM-dd")


        if not nombre or not tipo_nombre:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios.")
            return

        id_tipo = Query.get_tipo_id(tipo_nombre)

        if id_tipo:
            Query.insert_data_instrument(nombre, id_tipo, fecha)
            self.lned_nombre.clear()
            QMessageBox.information(self, "Éxito", "Instrumento guardado exitosamente.")
            self.data_updater.update_data()

        else:
            QMessageBox.warning(self, "Error", "No se pudo encontrar el tipo de instrumento.")


    def actualizar_tabla(self):
        self.tabla_instrumentos.update_table()