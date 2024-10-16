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

        self.parametros_por_tipo = {
            'PIEZÓMETRO': ['cb', 'angulo'],
            'FREATÍMETRO': ['cb', 'angulo'],
            'AFORADOR PARSHALL': ['u', 'k'],
            'AFORADOR VOLUMÉTRICO': [],
        }

        self.campos_parametros = {
            'cb': self.lned_cb,
            'angulo': self.lned_angulo,
            'u': self.lned_u,
            'k': self.lned_k,
        }
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

        #
        self.lbl_cb = QLabel("Cota superior: cb", self)
        self.lned_cb = QLineEdit(self)
        self.lned_cb.setFixedWidth(180)

        self.lbl_angulo = QLabel("Angulo cenital", self)
        self.lned_angulo = QLineEdit(self)
        self.lned_angulo.setFixedWidth(180)

        self.lbl_u = QLabel("u", self)
        self.lned_u = QLineEdit(self)
        self.lned_u.setFixedWidth(180)

        self.lbl_k = QLabel("K", self)
        self.lned_k = QLineEdit(self)
        self.lned_k.setFixedWidth(180)

        self.lbl_u.hide()
        self.lned_u.hide()
        self.lbl_k.hide()
        self.lned_k.hide()
        #
        self.btn_guardar = QPushButton("Guardar", self)
        self.btn_guardar.setFixedWidth(160)
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
        grid_layout.setRowStretch(12, 1)
        grid_layout.setRowStretch(14, 1)

        grid_layout.addWidget(lbl_titulo_ppal, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 3, 0)
        grid_layout.addWidget(lbl_nombre, 3, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_nombre, 3, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v2, 3, 3)
        grid_layout.addWidget(lbl_tipo, 5, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmb_tipe, 5, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_fecha, 7, 1, 1, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.date_edit, 7, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_cb, 9, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_cb, 9, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_angulo, 11, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_angulo, 11, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_k, 9, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_k, 9, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lbl_u, 11, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.lned_u, 11, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_guardar, 13, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 15, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.cmb_tipe.currentIndexChanged.connect(self.mostrar_parametros)
        self.btn_guardar.clicked.connect(self.guardar)

    def mostrar_parametros(self):
        for label, campo in self.campos_parametros.items():
            label_widget = getattr(self, f'lbl_{label}')
            label_widget.hide()
            campo.hide()

        tipo_seleccionado = self.cmb_tipe.currentText()
        if tipo_seleccionado in self.parametros_por_tipo:
            parametros = self.parametros_por_tipo[tipo_seleccionado]
            for parametro in parametros:
                label_widget = getattr(self, f'lbl_{parametro}')
                campo = self.campos_parametros[parametro]
                label_widget.show()
                campo.show()
    def guardar(self):
        nombre = self.lned_nombre.text().strip()
        tipo_nombre = self.cmb_tipe.currentText().strip()
        fecha = self.date_edit.date().toString("yyyy-MM-dd")

        if not nombre or not tipo_nombre:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios.")
            return

        id_tipo = Query.get_tipo_id(tipo_nombre)
        if not id_tipo:
            QMessageBox.warning(self, "Error", "No se pudo encontrar el tipo de instrumento.")
            return


        Query.insert_data_instrument(nombre, id_tipo, fecha)
        id_instrumento = Query.get_ultimo_id_instrumento()

        if not id_instrumento:
            QMessageBox.critical(self, "Error", "No se pudo insertar el instrumento.")
            return

        parametros_a_guardar = self.parametros_por_tipo.get(tipo_nombre, [])
        for parametro in parametros_a_guardar:
            campo = self.campos_parametros[parametro]
            valor = campo.text().strip()
            if valor:
                Query.insert_data_parametro(id_instrumento, parametro, valor)

        self.lned_nombre.clear()
        self.lned_angulo.clear()
        self.lned_u.clear()
        self.lned_cb.clear()
        self.lned_k.clear()
        QMessageBox.information(self, "Éxito", "Instrumento guardado exitosamente.")
        self.data_updater.update_data()


    def actualizar_tabla(self):
        self.tabla_instrumentos.update_table()