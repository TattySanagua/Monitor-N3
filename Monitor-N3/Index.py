from PyQt5.QtWidgets import QApplication, QAction, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from View.HomeView import HomeView
from View.PiezometersView import PiezometersView
from View.FreatimeterView import FreatimeterView
from View.AforadoresView import AforadoresView
from View.TablePiezometerView import TablaPiezometrosView
from View.TableFreatimiterView import TablaFreatimetroView
from View.TableAforadorView import TablaAforadoresView
import sys

class Monitor(QMainWindow):

    data_updated_signal = pyqtSignal()
    def __init__(self):
        super(Monitor, self).__init__()
        self.setWindowTitle("Monitor N3")
        # screen_size = QDesktopWidget().screenGeometry()
        self.setGeometry(50, 50, 450, 650)
        self.setWindowIcon(QIcon("LogoOrsep.jpg"))
        self.create_menu()
        self.central_widget = HomeView()
        self.setCentralWidget(self.central_widget)

        self.tabla_freatimetro_view = TablaFreatimetroView()
        self.freatimeter_view = FreatimeterView(self.tabla_freatimetro_view)

        self.tabla_embalse_7piezometros = TablaPiezometrosView()
        self.piezometers_view = PiezometersView(self.tabla_embalse_7piezometros)

        self.tabla_embalse_aforadores = TablaAforadoresView()
        self.aforadores_view = AforadoresView(self.tabla_embalse_aforadores)

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

        action_piezometros = QAction("Medición", self)
        action_piezometros.triggered.connect(self.show_piezometros_view)
        menu_piezometros.addAction(action_piezometros)

        action_piezometros = QAction("Tabla", self)
        action_piezometros.triggered.connect(self.show_tablas_piezometros_view)
        menu_piezometros.addAction(action_piezometros)

        action_piezometros = QAction("Gráfico", self)
        action_piezometros.triggered.connect(self.show_grafico_piezometro_view)
        menu_piezometros.addAction(action_piezometros)

        action_freatimetro = QAction("Medición", self)
        action_freatimetro.triggered.connect(self.show_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        action_freatimetro = QAction("Tabla", self)
        action_freatimetro.triggered.connect(self.show_tabla_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        action_freatimetro = QAction("Gráfico", self)
        action_freatimetro.triggered.connect(self.show_grafico_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        action_aforadores = QAction("Medición", self)
        action_aforadores.triggered.connect(self.show_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

        action_aforadores = QAction("Tabla", self)
        action_aforadores.triggered.connect(self.show_tablas_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

        action_aforadores = QAction("Gráfico", self)
        action_aforadores.triggered.connect(self.show_grafico_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

    def show_home_view(self):
        self.central_widget = HomeView()
        self.setCentralWidget(self.central_widget)
    def show_piezometros_view(self):
        self.central_widget = PiezometersView(self.tabla_embalse_7piezometros)
        self.setCentralWidget(self.central_widget)

    def show_tablas_piezometros_view(self):
        if not self.tabla_embalse_7piezometros:
            self.tabla_embalse_7piezometros = TablaPiezometrosView()
        self.tabla_embalse_7piezometros.show()

    def show_grafico_piezometro_view(self):
        pass

    def show_freatimetro_view(self):
        self.central_widget = FreatimeterView(self.tabla_freatimetro_view)
        self.setCentralWidget(self.central_widget)

    def show_tabla_freatimetro_view(self):
        if not self.tabla_freatimetro_view:
            self.tabla_freatimetro_view = TablaFreatimetroView()
        self.tabla_freatimetro_view.show()

    # def update_tabla_freatimetro(self):
    #     if self.tabla_freatimetro_view:
    #         self.tabla_freatimetro_view.update_table()

    def show_grafico_freatimetro_view(self):
        pass

    def show_aforadores_view(self):
        self.central_widget = AforadoresView(self.tabla_embalse_aforadores)
        self.setCentralWidget(self.central_widget)

    def show_tablas_aforadores_view(self):
        if not self.tabla_embalse_aforadores:
            self.tabla_embalse_aforadores = TablaAforadoresView()
        self.tabla_embalse_aforadores.show()

    def show_grafico_aforadores_view(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Monitor()
    window.show()
    sys.exit(app.exec_())