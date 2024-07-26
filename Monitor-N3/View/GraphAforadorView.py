from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox, QWidget, QLabel, QComboBox, QGridLayout
from DataBase.Query import Query
import pandas as pd
import plotly.graph_objects as go

class GraphAforadorView(QWidget):
    def __init__(self):
        super(GraphAforadorView, self).__init__()
        self.setWindowTitle("Gráficos Aforadores")
        self.setGeometry(300, 130, 400, 400)
        self.init_ui()

    def init_ui(self):
        lbl_select = QLabel("Seleccionar tipo de gráfico", self)
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")
        self.cmb_grafic = QComboBox(self)

        self.cmb_grafic.addItems([
            "Afo3-TOT (Nivel embalse - Caudal)", #Dispersion
            "Afo3-TOT (Fecha - Nivel embalse - Caudal)", #Lineal, 3 ejes x:fecha, yizq:nivel embalse, yder:caudal
            "Afo3-EI (Nivel embalse - Caudal)", #Dispersion
            "Afo3-PP (Nivel embalse - Caudal)", #Dispersion
            "Afo3-PP (Fecha - Nivel embalse - Caudal)" #Lineal, 3 ejes x:fecha, yizq:nivel embalse, yder:caudal
        ])

        self.btn_generate = QPushButton("Graficar")

        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout(self)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(3, 1)
        grid_layout.setRowStretch(5, 1)

        grid_layout.addWidget(lbl_v1, 1, 0)
        grid_layout.addWidget(lbl_select, 1, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(lbl_v2, 1, 3)
        grid_layout.addWidget(self.cmb_grafic, 2, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(self.btn_generate, 4, 1, 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(footer_label, 6, 1, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(grid_layout)

        self.btn_generate.clicked.connect(self.show_selected_graph)

    def show_selected_graph(self):
        selected_graph = self.cmb_grafic.currentText()
        if selected_graph.startswith("Afo3-TOT (Fecha") or selected_graph.startswith("Afo3-PP (Fecha"):
            self.show_graph(selected_graph, mode='lines+markers')
        else:
            self.show_graph(selected_graph, mode='markers')

    def show_graph(self, graph_type, mode):
        data = None
        x_column = 'nivel_embalse'
        y_columns = ['caudal']
        title = graph_type.split(' (')[0]
        x_title = 'N.E[msnm]'
        y_title = 'Caudal'

        if graph_type == "Afo3-TOT (Nivel embalse - Caudal)":
            data = Query.get_afo3_tot()
        elif graph_type == "Afo3-EI (Nivel embalse - Caudal)":
            data = Query.get_afo3_ei()
        elif graph_type == "Afo3-PP (Nivel embalse - Caudal)":
            data = Query.get_afo3_pp()
        elif graph_type == "Afo3-TOT (Fecha - Nivel embalse - Caudal)":
            data = Query.get_afo3_tot()
            x_column = 'fecha'
            y_columns = ['nivel_embalse', 'caudal']
            x_title = 'Fecha'
        elif graph_type == "Afo3-PP (Fecha - Nivel embalse - Caudal)":
            data = Query.get_afo3_pp()
            y_columns = ['nivel_embalse', 'caudal']
            x_column = 'fecha'
            x_title = 'Fecha'

        if data is None or len(data) == 0:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)
        df = df.dropna(subset=[x_column] + y_columns)
        fig = go.Figure()

        if x_column == 'fecha':
            # para gráficos cronológicos con dos ejes Y
            fig.add_trace(
                go.Scatter(x=df[x_column], y=df['nivel_embalse'], mode=mode, name='Nivel embalse', yaxis='y1'))
            fig.add_trace(go.Scatter(x=df[x_column], y=df['caudal'], mode=mode, name='Caudal', yaxis='y2'))
            fig.update_layout(
                title=title,
                xaxis=dict(
                    title=x_title,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1month", step="month", stepmode="backward"),
                            dict(count=6, label="6month", step="month", stepmode="backward"),
                            dict(count=1, label="YearTodate", step="year", stepmode="todate"),
                            dict(count=1, label="1year", step="year", stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(visible=True),
                    type="date"
                ),
                yaxis=dict(title='Nivel embalse [msnm]', showgrid=True),
                yaxis2=dict(title='Caudal [l/s]', overlaying='y', side='right', showgrid=False)
            )
        else:
            # gráficos no cronológicos
            for y_column in y_columns:
                fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], mode=mode, name=y_column))
            fig.update_layout(
                title=title,
                xaxis_title=x_title,
                yaxis_title=y_title,
                legend_title='Aforadores',
                xaxis=dict(rangeslider=dict(visible=True))
            )
        fig.show()