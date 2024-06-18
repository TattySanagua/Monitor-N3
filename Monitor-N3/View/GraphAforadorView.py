from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox
from DataBase.Query import Query
from View.GraphView import GraphView
import pandas as pd
import plotly.graph_objects as go

class GraphAforadorView(GraphView):
    def __init__(self):
        super(GraphAforadorView, self).__init__()
        self.setWindowTitle("Gráficos Aforadores")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        self.hlyt_buttons = QHBoxLayout()
        self.btn_afo3_tot_ne_caudal = QPushButton("Afo3-TOT - N.E - Caudal")
        self.btn_afo3_tot_fecha_ne_caudal = QPushButton("Afo3-TOT Cronológico")
        self.btn_afo3_ei_ne_caudal = QPushButton("Afo3-EI - N.E - Caudal")
        self.btn_afo3_pp_ne_caudal = QPushButton("Afo3-PP - N.E - Caudal")
        self.btn_afo3_pp_fecha_ne_caudal = QPushButton("Afo3-PP Cronológico")

        self.hlyt_buttons.addWidget(self.btn_afo3_tot_ne_caudal)
        self.hlyt_buttons.addWidget(self.btn_afo3_tot_fecha_ne_caudal)
        self.hlyt_buttons.addWidget(self.btn_afo3_ei_ne_caudal)
        self.hlyt_buttons.addWidget(self.btn_afo3_pp_ne_caudal)
        self.hlyt_buttons.addWidget(self.btn_afo3_pp_fecha_ne_caudal)

        self.btn_afo3_tot_ne_caudal.clicked.connect(self.show_graph_afo3_tot_ne_caudal)
        self.btn_afo3_tot_fecha_ne_caudal.clicked.connect(self.show_graph_afo3_tot_fecha_ne_caudal)
        self.btn_afo3_ei_ne_caudal.clicked.connect(self.show_graph_afo3_ei_ne_caudal)
        self.btn_afo3_pp_ne_caudal.clicked.connect(self.show_graph_afo3_pp_ne_caudal)
        self.btn_afo3_pp_fecha_ne_caudal.clicked.connect(self.show_graph_afo3_pp_fecha_ne_caudal)

        self.layout.addLayout(self.hlyt_buttons)

    def show_graph_afo3_tot_ne_caudal(self):
        data = Query.get_afo3_tot()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['caudal'], mode='markers'))

        fig.update_layout(title='AFO3-TOT', xaxis_title='Nivel de Embalse', yaxis_title='Caudal')

        fig.show()

    def show_graph_afo3_tot_fecha_ne_caudal(self):
        data = Query.get_afo3_tot()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_embalse'], mode='lines+markers', name='Afo3-Tot', yaxis='y1'))
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['caudal'], mode='lines+markers', name='Nivel embalse', yaxis='y2'))

        fig.update_layout(
            title='Cronológico: Afo3-Tot - Nivel de embalse',
            xaxis=dict(title='Fecha'),
            yaxis=dict(title='Nivel embalse [msnm]'),
            yaxis2=dict(
                title='Caudal[l/s]',
                titlefont=dict(color='red'),
                tickfont=dict(color='red'),
                overlaying='y',
                side='right'),
            legend=dict(
                x=0.5,
                xanchor='center',
                y=1.1,
                orientation='h'
            )
        )

        fig.show()
    def show_graph_afo3_ei_ne_caudal(self):
        data = Query.get_afo3_ei()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['caudal'], mode='markers'))

        fig.update_layout(title='AFO3-EI', xaxis_title='Nivel de Embalse', yaxis_title='Caudal')

        fig.show()

    def show_graph_afo3_pp_ne_caudal(self):
        data = Query.get_afo3_pp()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['caudal'], mode='markers'))

        fig.update_layout(title='AFO3-PP', xaxis_title='Nivel de Embalse', yaxis_title='Caudal')

        fig.show()


    def show_graph_afo3_pp_fecha_ne_caudal(self):
        data = Query.get_afo3_pp()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_embalse'], mode='lines+markers', name='Afo3-PP', yaxis='y1'))
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['caudal'], mode='lines+markers', name='Nivel embalse', yaxis='y2'))

        fig.update_layout(
            title='Cronológico: Afo3-PP - Nivel de embalse',
            xaxis=dict(
                title='Fecha',
                showgrid=True
            ),
            yaxis=dict(
                title='Nivel embalse [msnm]',
                titlefont=dict(color='blue'),
                tickfont=dict(color='blue'),
                showgrid=True
            ),
            yaxis2=dict(
                title='Caudal[l/s]',
                titlefont=dict(color='red'),
                tickfont=dict(color='red'),
                overlaying='y',
                side='right',
                showgrid=True
            ),
            legend=dict(
                x=0.5,
                xanchor='center',
                y=1.1,
                orientation='h'
            )
        )

        fig.show()