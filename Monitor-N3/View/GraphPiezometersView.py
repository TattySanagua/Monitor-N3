from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox, QComboBox, QGridLayout, QWidget, QLabel
from DataBase.Query import Query
from View.GraphView import GraphView
import pandas as pd
import plotly.graph_objects as go

class GraphPiezometrosView(QWidget):
    def __init__(self):
        super(GraphPiezometrosView, self).__init__()
        self.setWindowTitle("Gráficos Piezómetros")
        self.setGeometry(300, 130, 500, 500)
        self.init_ui()

    def init_ui(self):

        lbl_select = QLabel("Seleccionar tipo de gráfico", self)
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")
        self.cmb_grafic = QComboBox(self)

        self.cmb_grafic.addItems([
            "L3-PC1 (Nivel embalse - Nivel piezométrico)",
            "L3-PC2 (Nivel embalse - Nivel piezométrico)",
            "L3-PC3 (Nivel embalse - Nivel piezométrico)",
            "L3-PC4 (Nivel embalse - Nivel piezométrico)",
            "L3-PC5 (Nivel embalse - Nivel piezométrico)",
            "L3-PC6 (Nivel embalse - Nivel piezométrico)",
            "L3-PC7 (Nivel embalse - Nivel piezométrico)",
            "PC1-5-6 (Fecha - Nivel piezométrico)",
            "PC1-5-6 (Nivel embalse - Nivel piezométrico)",
            "F1-PC2-3-4 (Fecha - Nivel piezométrico)",
            "F1-PC2-3-4 (Nivel embalse - Nivel piezométrico)"
        ])

        self.btn_generate = QPushButton("Graficar")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(5, 1)

        grid_layout.addWidget(lbl_v1, 1, 0)
        grid_layout.addWidget(lbl_select, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v2, 1, 3)
        grid_layout.addWidget(self.cmb_grafic, 2, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_generate, 4, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_generate.clicked.connect(self.show_selected_graph)

    def show_selected_graph(self):
        selected_graph = self.cmb_grafic.currentText()
        if selected_graph.startswith("L3-PC") or selected_graph.startswith("PC1-5-6 (Nivel") or selected_graph.startswith("F1-PC2-3-4 (Nivel"):
            self.show_graph(selected_graph, mode='markers')
        elif selected_graph.startswith("PC1-5-6 (Fecha") or selected_graph.startswith("F1-PC2-3-4 (Fecha"):
            self.show_graph(selected_graph, mode='lines+markers')

    def show_graph(self, graph_type, mode):
        pass
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