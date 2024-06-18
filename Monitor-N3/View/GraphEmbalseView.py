from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox
from DataBase.Query import Query
from View.GraphView import GraphView
import pandas as pd
import plotly.graph_objects as go

class GraphEmbalseView(GraphView):
    def __init__(self):
        super(GraphEmbalseView, self).__init__()
        self.setWindowTitle("Gráficos Embalse")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        self.hlyt_buttons = QHBoxLayout()
        self.btn_ne_tiempo = QPushButton("N.E - Tiempo")

        self.hlyt_buttons.addWidget(self.btn_ne_tiempo)

        self.btn_ne_tiempo.clicked.connect(self.show_graph_ne_tiempo)

        self.layout.addLayout(self.hlyt_buttons)

    def show_graph_ne_tiempo(self):
        data = Query.get_embalse()
        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_embalse'], mode='lines+markers'))
        fig.update_layout(title='Embalse', xaxis_title='Fecha', yaxis_title='N.E[msnm]')
        fig.show()

