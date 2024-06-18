from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox
from DataBase.Query import Query
from View.GraphView import GraphView
import pandas as pd
import plotly.graph_objects as go

class GraphFreatimeterView(GraphView):
    def __init__(self):
        super(GraphFreatimeterView, self).__init__()
        self.setWindowTitle("Gráficos Freatimetro")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        self.hlyt_buttons = QHBoxLayout()
        self.btn_ne_nf = QPushButton("x=N.E - y=Nivel Freático")

        self.hlyt_buttons.addWidget(self.btn_ne_nf)

        self.btn_ne_nf.clicked.connect(self.show_graph_ne_nf)

        self.layout.addLayout(self.hlyt_buttons)

    def show_graph_ne_nf(self):
        data = Query.get_l3_f1()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_freatico'], mode='markers', name='markers'))

        fig.update_layout(title='L3-F1', xaxis_title='Nivel de Embalse', yaxis_title='Nivel Freático')

        fig.show()
