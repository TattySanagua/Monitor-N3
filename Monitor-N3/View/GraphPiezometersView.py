from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QMessageBox, QComboBox, QGridLayout, QWidget, QLabel
from DataBase.Query import Query
import pandas as pd
import plotly.graph_objects as go

class GraphPiezometrosView(QWidget):
    def __init__(self):
        super(GraphPiezometrosView, self).__init__()
        self.setWindowTitle("Gráficos Piezómetros")
        self.setGeometry(300, 130, 400, 400)
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
            "L3-PC7 (Fecha - Nivel piezométrico)",
            "PC1-5-6 (Fecha - Nivel piezométrico)",
            "PC1-5-6 (Nivel embalse - Nivel piezométrico)",
            "F1-PC2-3-4 (Fecha - Nivel piezométrico)",
            "F1-PC2-3-4 (Nivel embalse - Nivel piezométrico)"
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
        if selected_graph.startswith("PC1-5-6 (Fecha") or selected_graph.startswith("F1-PC2-3-4 (Fecha") or selected_graph.startswith("L3-PC7 (Fecha"):
            self.show_graph(selected_graph, mode='lines+markers')
        else:
            self.show_graph(selected_graph, mode='markers')

    def show_graph(self, graph_type, mode):
        data = None
        x_column = 'nivel_embalse'
        y_columns = ['nivel_piezometrico']
        title = graph_type.split(' (')[0]
        x_title = 'N.E[msnm]'
        y_title = 'NP'

        if graph_type == "L3-PC1 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc1()
        elif graph_type == "L3-PC2 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc2()
        elif graph_type == "L3-PC3 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc3()
        elif graph_type == "L3-PC4 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc4()
        elif graph_type == "L3-PC5 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc5()
        elif graph_type == "L3-PC6 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc6()
        elif graph_type == "L3-PC7 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_l3_pc7()
        elif graph_type == "L3-PC7 (Fecha - Nivel piezométrico)":
            data = Query.get_l3_pc7()
            x_column = 'fecha'
            y_columns = ['nivel_embalse', 'nivel_piezometrico']
            x_title = 'Fecha'
        elif graph_type == "PC1-5-6 (Fecha - Nivel piezométrico)" or graph_type == "PC1-5-6 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_embalse_pc1_5_6()
            y_columns = ['nivel_embalse', 'nivel_piezometrico_pc1', 'nivel_piezometrico_pc5', 'nivel_piezometrico_pc6']
            if graph_type == "PC1-5-6 (Fecha - Nivel piezométrico)":
                x_column = 'fecha'
                x_title = 'Fecha'
        elif graph_type == "F1-PC2-3-4 (Fecha - Nivel piezométrico)" or graph_type == "F1-PC2-3-4 (Nivel embalse - Nivel piezométrico)":
            data = Query.get_embalse_f1_pc2_pc3_pc4()
            y_columns = ['nivel_freatico', 'nivel_piezometrico_pc2', 'nivel_piezometrico_pc3', 'nivel_piezometrico_pc4']
            if graph_type == "F1-PC2-3-4 (Fecha - Nivel piezométrico)":
                x_column = 'fecha'
                x_title = 'Fecha'

        if data is None or len(data) == 0:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        df = pd.DataFrame(data)
        df = df.dropna(subset=[x_column] + y_columns)
        fig = go.Figure()

        for y_column in y_columns:
            fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], mode=mode, name=y_column))

        if x_column == 'fecha':
            # para gráficos cronológicos
            fig.update_layout(
                title=title,
                xaxis_title=x_title,
                yaxis_title=y_title,
                legend_title='Piezómetros',
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1month", step="month", stepmode="backward"),
                            dict(count=6, label="6month", step="month", stepmode="backward"),
                            dict(count=1, label="YearTodate", step="year", stepmode="todate"),
                            dict(count=1, label="1year", step="year", stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(
                        visible=True
                    ),
                    type="date"
                )
            )
        else:
            # gráficos no cronológicos
            fig.update_layout(
                title=title,
                xaxis_title=x_title,
                yaxis_title=y_title,
                legend_title='Piezómetros',
                xaxis=dict(
                    rangeslider=dict(
                        visible=True
                    )
                )
            )
        fig.show()
