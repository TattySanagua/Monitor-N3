from PyQt5.QtWidgets import QPushButton, QMessageBox, QComboBox, QLabel, QGridLayout, QWidget
from DataBase.Query import Query
from PyQt5.QtCore import Qt
from View.GraphView import GraphView
import pandas as pd
import plotly.graph_objects as go

class GraphEmbalseView(QWidget):
    def __init__(self):
        super(GraphEmbalseView, self).__init__()
        self.setWindowTitle("Gráficos Embalse")
        self.setGeometry(300, 130, 400, 400)
        self.init_ui()

    def init_ui(self):

        lbl_select = QLabel("Seleccionar tipo de gráfico", self)
        self.cmb_grafic = QComboBox(self)
        self.cmb_grafic.addItems(["Nivel embalse - Tiempo"])
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")

        self.btn_generate = QPushButton("Graficar")

        grid_layout = QGridLayout()

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(5, 1)

        grid_layout.addWidget(lbl_v1, 1, 0)
        grid_layout.addWidget(lbl_select, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v2, 1, 3)
        grid_layout.addWidget(self.cmb_grafic, 2, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_generate, 4, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_generate.clicked.connect(self.show_graph)

    def show_graph(self):
        data = Query.get_embalse()
        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_embalse'], mode='lines+markers'))
        fig.update_layout(
            title='Embalse',
            xaxis_title='Fecha',
            yaxis_title='N.E[msnm]',
            xaxis=dict(rangeslider=dict(visible=True), type="date")
        )
        fig.show()

