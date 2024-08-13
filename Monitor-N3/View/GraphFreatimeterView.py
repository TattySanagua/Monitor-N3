from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox, QWidget, QLabel, QComboBox, QGridLayout
from DataBase.Query import Query
import pandas as pd
import plotly.graph_objects as go

class GraphFreatimeterView(QWidget):
    def __init__(self):
        super(GraphFreatimeterView, self).__init__()
        self.setWindowTitle("Gráficos Freatimetro")
        self.setGeometry(300, 130, 400, 400)
        self.init_ui()

    def init_ui(self):
        lbl_select = QLabel("Seleccionar tipo de gráfico", self)
        self.cmb_grafic = QComboBox(self)
        self.cmb_grafic.addItems(["Nivel embalse - Nivel freático"])
        lbl_v1 = QLabel("")
        lbl_v2 = QLabel("")
        self.btn_generate = QPushButton("Graficar")

        footer_label = QLabel("© 2024 Tatiana Sanagua - ORSEP. All rights reserved.")
        footer_label.setStyleSheet("font-size: 12px; color: gray;")

        grid_layout = QGridLayout()

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

        self.btn_generate.clicked.connect(self.show_graph)


    def show_graph(self):
        data = Query.get_l3_f1()

        if data.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)

        # Asegurarse de que la columna 'fecha' está en formato datetime
        df['fecha'] = pd.to_datetime(df['fecha'])
        df = df.dropna(subset=['fecha', 'nivel_embalse', 'nivel_freatico'])

        # Obtener los años únicos en los datos
        unique_years = df['fecha'].dt.year.unique()
        fig = go.Figure()

        # Iterar sobre cada año y agregar una traza diferente
        for year in unique_years:
            df_year = df[df['fecha'].dt.year == year]
            fig.add_trace(go.Scatter(
                x=df_year['nivel_embalse'],
                y=df_year['nivel_freatico'],
                mode='markers',
                name=str(year),
                marker=dict(size=10)
            ))

        fig.update_layout(
            title='L3-F1',
            xaxis_title='Nivel de Embalse',
            yaxis_title='Nivel Freático',
            xaxis=dict(
                rangeslider=dict(visible=True)
            ),
            legend_title='Años'
        )

        fig.show()
