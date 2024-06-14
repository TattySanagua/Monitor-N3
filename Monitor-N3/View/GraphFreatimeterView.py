from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMessageBox
from DataBase.Query import Query
from View.GraphView import GraphView
from View.ShowGraphEmbalse import ShowGraph

class GraphFreatimeterView(GraphView):
    def __init__(self):
        super(GraphFreatimeterView, self).__init__()
        self.setWindowTitle("Gráficos Freatimetro")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        super().init_ui()
        self.hlyt_buttons = QHBoxLayout()
        self.btn_ne_tiempo = QPushButton("N.E - Nivel Freático")
        #self.btn_ne_lluvia = QPushButton("N.E - Precipitación")

        self.hlyt_buttons.addWidget(self.btn_ne_tiempo)
        #self.hlyt_buttons.addWidget(self.btn_ne_lluvia)

        self.btn_ne_tiempo.clicked.connect(self.show_graph_ne_tiempo)
        #self.btn_ne_lluvia.clicked.connect(self.show_graph_ne_lluvia)

        self.layout.addLayout(self.hlyt_buttons)

    def show_graph_ne_tiempo(self):
        df = Query.get_l3_f1()
        if df.empty:
            QMessageBox.warning(self, "Advertencia", "No hay datos disponibles para mostrar.")
            return

        self.show_graph(df, "Nivel de embalse - Nivel Freático", "Nivel de Embalse", "Nivel Freático")

    # def show_graph_ne_lluvia(self):
    #     pass

    def show_graph(self, df, title, xlabel, ylabel):
        self.graph_window = ShowGraph(df, title, xlabel, ylabel)
        self.graph_window.showFullScreen()