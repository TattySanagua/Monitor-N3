from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, \
    QDesktopWidget, QMessageBox, QDateTimeEdit, QAction, QMainWindow
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QIcon
from HomeView import HomeView
from PiezometersView import PiezometersView
from FreatimeterView import FreatimeterView
from AforadoresView import AforadoresView
import sys

class Monitor(QMainWindow):

    def __init__(self):
        super(Monitor, self).__init__()
        self.setWindowTitle("Monitor N3")
        # screen_size = QDesktopWidget().screenGeometry()
        self.setGeometry(50, 50, 600, 650)
        self.setWindowIcon(QIcon("../LogoOrsep.jpg"))
        self.create_menu()
        self.central_widget = HomeView()
        self.setCentralWidget(self.central_widget)


    def create_menu(self):
        #Menu bar
        menu_bar = self.menuBar()
        menu_inicio = menu_bar.addMenu("Inicio")
        menu_piezometros = menu_bar.addMenu("Piezómetros")
        menu_freatimetro = menu_bar.addMenu("Freatímetro")
        menu_aforadores = menu_bar.addMenu("Aforadores")

        #Acciones
        action_inicio = QAction("Inicio", self)
        action_inicio.triggered.connect(self.show_home_view)
        menu_inicio.addAction(action_inicio)

        action_piezometros = QAction("Piezómetros", self)
        action_piezometros.triggered.connect(self.show_piezometros_view)
        menu_piezometros.addAction(action_piezometros)

        action_freatimetro = QAction("Freatímetro", self)
        action_freatimetro.triggered.connect(self.show_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        action_aforadores = QAction("Aforadores", self)
        action_aforadores.triggered.connect(self.show_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

    def show_home_view(self):
        self.central_widget = HomeView()
        self.setCentralWidget(self.central_widget)
    def show_piezometros_view(self):
        self.central_widget = PiezometersView()
        self.setCentralWidget(self.central_widget)

    def show_freatimetro_view(self):
        self.central_widget = FreatimeterView()
        self.setCentralWidget(self.central_widget)

    def show_aforadores_view(self):
        self.central_widget = AforadoresView()
        self.setCentralWidget(self.central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Monitor()
    window.show()
    sys.exit(app.exec_())