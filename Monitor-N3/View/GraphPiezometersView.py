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
        self.btn_pc1_5_6_fecha_np = QPushButton("PC1-5-6 (Fecha - NP)") #Lineal
        self.btn_pc1_5_6_ne_np = QPushButton("PC1-5-6 (N.E - NP)")
        self.btn_f1_pc2_3_4_fecha_np = QPushButton("F1-PC2-3-4 (Fecha - NP)")
        self.btn_f1_pc2_3_4_ne_np = QPushButton("F1-PC2-3-4 (N.E - NP)")


        self.hlyt_buttons.addWidget(self.btn_pc1)
        self.hlyt_buttons.addWidget(self.btn_pc2)
        self.hlyt_buttons.addWidget(self.btn_pc3)
        self.hlyt_buttons.addWidget(self.btn_pc4)
        self.hlyt_buttons.addWidget(self.btn_pc5)
        self.hlyt_buttons.addWidget(self.btn_pc6)
        self.hlyt_buttons.addWidget(self.btn_pc7)
        self.hlyt_buttons.addWidget(self.btn_pc1_5_6_fecha_np)
        self.hlyt_buttons.addWidget(self.btn_pc1_5_6_ne_np)
        self.hlyt_buttons.addWidget(self.btn_f1_pc2_3_4_fecha_np)
        self.hlyt_buttons.addWidget(self.btn_f1_pc2_3_4_ne_np)

        self.btn_pc1.clicked.connect(self.show_graph_pc1)
        self.btn_pc2.clicked.connect(self.show_graph_pc2)
        self.btn_pc3.clicked.connect(self.show_graph_pc3)
        self.btn_pc4.clicked.connect(self.show_graph_pc4)
        self.btn_pc5.clicked.connect(self.show_graph_pc5)
        self.btn_pc6.clicked.connect(self.show_graph_pc6)
        self.btn_pc7.clicked.connect(self.show_graph_pc7)
        self.btn_pc1_5_6_fecha_np.clicked.connect(self.show_graph_pc1_5_6_fecha_np)
        self.btn_pc1_5_6_ne_np.clicked.connect(self.show_graph_pc1_5_6_ne_np)
        self.btn_f1_pc2_3_4_fecha_np.clicked.connect(self.show_graph_f1_pc2_3_4_fecha_np)
        self.btn_f1_pc2_3_4_ne_np.clicked.connect(self.show_graph_f1_pc2_3_4_ne_np)

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

    def show_graph_pc1_5_6_fecha_np(self):
        data = Query.get_embalse_pc1_5_6()
        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['fecha'], y=df['nivel_embalse'], mode='lines+markers', name='Nivel ambalse'))

        df_pc1 = df.dropna(subset=['nivel_piezometrico_pc1'])
        df_pc5 = df.dropna(subset=['nivel_piezometrico_pc5'])
        df_pc6 = df.dropna(subset=['nivel_piezometrico_pc6'])

        fig.add_trace(go.Scatter(x=df_pc1['fecha'], y=df_pc1['nivel_piezometrico_pc1'], mode='lines+markers', name='PC1'))
        fig.add_trace(go.Scatter(x=df_pc5['fecha'], y=df_pc5['nivel_piezometrico_pc5'], mode='lines+markers', name='PC5'))
        fig.add_trace(go.Scatter(x=df_pc6['fecha'], y=df_pc6['nivel_piezometrico_pc6'], mode='lines+markers', name='PC6'))

        fig.update_layout(title='Cronológico PC1-5-6 - Nivel embalse', xaxis_title='Fecha', yaxis_title='NP', legend_title='Piezómetros')

        fig.show()

    def show_graph_pc1_5_6_ne_np(self):
        data = Query.get_embalse_pc1_5_6()
        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico_pc1'], mode='lines+markers', name='PC1'))
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico_pc5'], mode='lines+markers', name='PC5'))
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico_pc6'], mode='lines+markers', name='PC6'))

        fig.update_layout(title='Dispersión PC1-5-6', xaxis_title='N.E[msnm]', yaxis_title='NP', legend_title='Piezómetros')
        fig.show()


    def show_graph_f1_pc2_3_4_fecha_np(self):
        data = Query.get_embalse_f1_pc2_pc3_pc4()
        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()

        df_f1 = df.dropna(subset=['nivel_freatico'])
        df_pc2 = df.dropna(subset=['nivel_piezometrico_pc2'])
        df_pc3 = df.dropna(subset=['nivel_piezometrico_pc3'])
        df_pc4 = df.dropna(subset=['nivel_piezometrico_pc4'])

        fig.add_trace(go.Scatter(x=df_f1['fecha'], y=df_f1['nivel_freatico'], mode='lines+markers', name='F1'))
        fig.add_trace(go.Scatter(x=df_pc2['fecha'], y=df_pc2['nivel_piezometrico_pc2'], mode='lines+markers', name='PC2'))
        fig.add_trace(go.Scatter(x=df_pc3['fecha'], y=df_pc3['nivel_piezometrico_pc3'], mode='lines+markers', name='PC3'))
        fig.add_trace(go.Scatter(x=df_pc4['fecha'], y=df_pc4['nivel_piezometrico_pc4'], mode='lines+markers', name='PC4'))

        fig.update_layout(title='Cronológico F1-PC2-3-4', xaxis_title='Fecha', yaxis_title='NF/NP', legend_title='Freatímetro - Piezómetros')

        fig.show()

    def show_graph_f1_pc2_3_4_ne_np(self):
        data = Query.get_embalse_f1_pc2_pc3_pc4()
        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_freatico'], mode='lines+markers', name='F1'))
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico_pc2'], mode='lines+markers', name='PC2'))
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico_pc3'], mode='lines+markers', name='PC3'))
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_piezometrico_pc4'], mode='lines+markers', name='PC4'))

        fig.update_layout(title='Dispersión F1-PC2-3-4', xaxis_title='N.E[msnm]', yaxis_title='NP', legend_title='Freatímetro - Piezómetros')

        fig.show()