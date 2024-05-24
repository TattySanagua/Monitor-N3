from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QDateEdit
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphView(QWidget):
    def __init__(self):
        super(GraphView, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self, x, y, title="", xlabel="", ylabel=""):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.canvas.draw()
