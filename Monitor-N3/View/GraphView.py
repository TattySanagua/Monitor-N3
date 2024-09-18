from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, \
    QMessageBox, QDateEdit, QComboBox, QCheckBox, QGridLayout, QListWidget

from DataBase.Query import Query


class GraphView(QWidget):
    def __init__(self):
        super(GraphView, self).__init__()
        self.init_ui()

    def init_ui(self):
        lbl_titulo_ppal = QLabel("Gráficos personalizados", self)
        lbl_titulo_ppal.setObjectName("title2")
        lbl_tipo_grafico = QLabel("Tipo de gráfico", self)
        lbl_eje_x = QLabel("Eje x", self)
        lbl_eje_y_1 = QLabel("Eje y1", self)
        lbl_v1 = QLabel(" ", self)
        lbl_v2 = QLabel(" ", self)

        self.cmb_tipo = QComboBox(self)
        self.cmb_tipo.setFixedWidth(180)
        self.cmb_tipo.addItems(["Lineal", "Puntos", "Barras"])

        self.cmb_x_axis = QComboBox(self)
        self.cmb_x_axis.setFixedWidth(180)
        self.cmb_x_axis.addItems(['Fecha', 'Nivel embalse', 'Caudal'])

        self.cmb_y_axis_1 = QComboBox(self)
        self.cmb_y_axis_1.setFixedWidth(180)
        self.cmb_y_axis_1.addItems(['Nivel embalse', 'Nivel piezométrico', 'Nivel freático', 'Caudal'])

        self.check_y_axis_2 = QCheckBox("Eje y2")
        self.cmb_y_axis_2 = QComboBox()
        self.cmb_y_axis_2.setEnabled(False)
        self.cmb_y_axis_2.addItems(['Nivel embalse', 'Nivel piezométrico', 'Nivel freático', 'Caudal'])

        self.instrumentos_list_y_1 = QListWidget()
        self.instrumentos_list_y_1.setSelectionMode(QListWidget.MultiSelection)


        self.update_instrumentos_list()

        self.btn_generar = QPushButton("Generar", self)
        self.btn_generar.setObjectName("btn")

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

        grid_layout.addWidget(lbl_titulo_ppal, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v1, 3, 0)
        grid_layout.addWidget(lbl_tipo_grafico, 3, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmb_tipo, 3, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_v2, 3, 3)
        grid_layout.addWidget(lbl_eje_x, 5, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmb_x_axis, 5, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(lbl_eje_y_1, 7, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmb_y_axis_1, 7, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.check_y_axis_2, 9, 1, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.cmb_y_axis_2, 9, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(self.btn_generar, 11, 2, 1, 2, alignment=Qt.AlignLeft)
        grid_layout.addWidget(footer_label, 13, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.check_y_axis_2.stateChanged.connect(self.toggle_secondary_y_axis)

        self.btn_generar.clicked.connect(self.generar)


    def update_instrumentos_list(self):
        tipo_y_1 = self.cmb_y_axis_1.currentText()

        if tipo_y_1 == 'Caudal':
            instumentos = Query.get_instrumentos("AFORADOR")

        ### Volver aqui cuando se haya modificado la estructura de la base de datos!!!!
        pass


    def generar(self):
        pass

    def toggle_secondary_y_axis(self, state):
        if state == 2:
            self.cmb_y_axis_2.setEnabled(True)
        else:
            self.cmb_y_axis_2.setEnabled(False)