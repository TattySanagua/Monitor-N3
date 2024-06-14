from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go

class ShowGraph(QDialog):
    def __init__(self, df, title, xlabel, ylabel):
        super(ShowGraph, self).__init__()
        self.setWindowTitle("Gráfico")
        self.init_ui(df, title, xlabel, ylabel)

    def init_ui(self, df, title, xlabel, ylabel):
        layout = QVBoxLayout()
        self.graph_view = QWebEngineView()

        # Crear el gráfico interactivo con Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['nivel_embalse'], y=df['nivel_freatico'], mode='markers'))
        fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)

        # Convertir el gráfico a HTML
        html = fig.to_html(full_html=False, include_plotlyjs='cdn')

        # Establecer el contenido HTML en la vista web
        self.graph_view.setHtml(html)

        layout.addWidget(self.graph_view)
        self.setLayout(layout)