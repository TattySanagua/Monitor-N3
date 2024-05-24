from PyQt5.QtWidgets import QDialog, QVBoxLayout
from View.GraphView import GraphView

class ShowGraph(QDialog):
    def __init__(self, x, y, title, xlabel, ylabel):
        super(ShowGraph, self).__init__()
        self.setWindowTitle("Gráfico")
        self.init_ui(x, y, title, xlabel, ylabel)

    def init_ui(self, x, y, title, xlabel, ylabel):
        self.graph_view = GraphView()
        self.graph_view.plot(x, y, title, xlabel, ylabel)

        layout = QVBoxLayout()
        layout.addWidget(self.graph_view)
        self.setLayout(layout)
