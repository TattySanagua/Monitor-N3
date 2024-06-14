from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox
from DataBase.Query import Query
from View.GraphView import GraphView
from View.ShowGraphEmbalse import ShowGraph

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
        self.btn_ne_lluvia = QPushButton("N.E - Precipitación")

        self.hlyt_buttons.addWidget(self.btn_ne_tiempo)
        self.hlyt_buttons.addWidget(self.btn_ne_lluvia)

        self.btn_ne_tiempo.clicked.connect(self.show_graph_ne_tiempo)
        self.btn_ne_lluvia.clicked.connect(self.show_graph_ne_lluvia)

        self.layout.addLayout(self.hlyt_buttons)

    def show_graph_ne_tiempo(self):
        df = Query.get_embalse()
        if df.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        self.show_graph(df, "Nivel de embalse - Tiempo", "Fecha", "N.E [msnm]")

    def show_graph_ne_lluvia(self):
        pass  # Implementa la lógica para otro tipo de gráfico aquí si es necesario

    def show_graph(self, df, title, xlabel, ylabel):
        self.graph_window = ShowGraph(df, title, xlabel, ylabel)
        self.graph_window.showFullScreen()  # O muestra de acuerdo a tus preferencias de visualización
