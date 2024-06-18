from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox
from DataBase.Query import Query
from View.GraphView import GraphView
import pandas as pd
import plotly.graph_objects as go

class GraphPiezometrosView(GraphView):
    def __init__(self):
        super(GraphPiezometrosView, self).__init__()
        self.setWindowTitle("Gráficos Piezómetros")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        self.hlyt_buttons = QHBoxLayout()

        self.btn_pc1 = QPushButton("L3-PC1 (N.E - NP)") #Dispersión
        self.btn_pc2 = QPushButton("L3-PC2 (N.E - NP)") #Dispersión
        self.btn_pc3 = QPushButton("L3-PC3 (N.E - NP)") #Dispersión
        self.btn_pc4 = QPushButton("L3-PC4 (N.E - NP)") #Dispersión
        self.btn_pc5 = QPushButton("L3-PC5 (N.E - NP)") #Dispersión
        self.btn_pc6 = QPushButton("L3-PC6 (N.E - NP)") #Dispersión
        self.btn_pc7 = QPushButton("L3-PC7 (N.E - NP)") #Lineal
        self.btn_pc1_5_6 = QPushButton("PC1-5-6 (Fecha - NP)") #Lineal

        self.hlyt_buttons.addWidget(self.btn_pc1)
        self.hlyt_buttons.addWidget(self.btn_pc2)
        self.hlyt_buttons.addWidget(self.btn_pc3)
        self.hlyt_buttons.addWidget(self.btn_pc4)
        self.hlyt_buttons.addWidget(self.btn_pc5)
        self.hlyt_buttons.addWidget(self.btn_pc6)
        self.hlyt_buttons.addWidget(self.btn_pc7)
        self.hlyt_buttons.addWidget(self.btn_pc1_5_6)

        self.btn_pc1.clicked.connect(self.show_graph_pc1)
        self.btn_pc2.clicked.connect(self.show_graph_pc2)
        self.btn_pc3.clicked.connect(self.show_graph_pc3)
        self.btn_pc4.clicked.connect(self.show_graph_pc4)
        self.btn_pc5.clicked.connect(self.show_graph_pc5)
        self.btn_pc6.clicked.connect(self.show_graph_pc6)
        self.btn_pc7.clicked.connect(self.show_graph_pc7)
        self.btn_pc1_5_6.clicked.connect(self.show_graph_pc1_5_6)

        self.layout.addLayout(self.hlyt_buttons)

    def show_graph_pc1(self):
        data = Query.get_l3_pc1()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico'], mode='markers'))
        fig.update_layout(title='L3-PC1', xaxis_title='N.E[msnm]', yaxis_title='NP')
        fig.show()

    def show_graph_pc2(self):
        data = Query.get_l3_pc2()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico'], mode='markers'))
        fig.update_layout(title='L3-PC2', xaxis_title='N.E[msnm]', yaxis_title='NP')
        fig.show()

    def show_graph_pc3(self):
        data = Query.get_l3_pc3()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico'], mode='markers'))
        fig.update_layout(title='L3-PC3', xaxis_title='N.E[msnm]', yaxis_title='NP')
        fig.show()

    def show_graph_pc4(self):
        data = Query.get_l3_pc4()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico'], mode='markers'))
        fig.update_layout(title='L3-PC4', xaxis_title='N.E[msnm]', yaxis_title='NP')
        fig.show()

    def show_graph_pc5(self):
        data = Query.get_l3_pc5()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico'], mode='markers'))
        fig.update_layout(title='L3-PC5', xaxis_title='N.E[msnm]', yaxis_title='NP')
        fig.show()

    def show_graph_pc6(self):
        data = Query.get_l3_pc6()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico'], mode='markers'))
        fig.update_layout(title='L3-PC6', xaxis_title='N.E[msnm]', yaxis_title='NP')
        fig.show()

    def show_graph_pc7(self):
        data = Query.get_l3_pc7()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_piezometrico'], mode='lines+markers'))
        fig.update_layout(title='L3-PC7', xaxis_title='Fecha', yaxis_title='NP')
        fig.show()

    def show_graph_pc1_5_6(self):
        data = Query.get_embalse_7piezometros()
        if not data:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data, columns=[
            'fecha', 'nivel_embalse', 'nivel_piezometrico_pc1', 'nivel_piezometrico_pc2',
            'nivel_piezometrico_pc3', 'nivel_piezometrico_pc4', 'nivel_piezometrico_pc5',
            'nivel_piezometrico_pc6', 'nivel_piezometrico_pc7'
        ])

        # df['fecha'] = pd.to_datetime(df['fecha'])

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_piezometrico_pc1'], mode='lines+markers'))
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_piezometrico_pc5'], mode='lines+markers'))
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_piezometrico_pc6'], mode='lines+markers'))

        fig.update_layout(title='Cronológico PC1-5-6', xaxis_title='Fecha', yaxis_title='NP', legend_title='Piezómetros')

        fig.show()