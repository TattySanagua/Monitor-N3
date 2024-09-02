from PyQt5.QtWidgets import QApplication, QAction, QMainWindow
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import pyqtSignal
from View.HomeView import HomeView
from View.EmbalseView import EmbalseView
from View.PrecipitacionView import PrecipitacionView
from View.PiezometersView import PiezometersView
from View.FreatimeterView import FreatimeterView
from View.AforadoresView import AforadoresView
from View.TableEmbalseView import TablaEmbalseView
from View.TablePiezometerView import TablaPiezometrosView
from View.TableFreatimeterView import TablaFreatimetroView
from View.TableAforadorView import TablaAforadoresView
from View.GraphEmbalseView import GraphEmbalseView
from View.GraphFreatimeterView import GraphFreatimeterView
from View.GraphPiezometersView import GraphPiezometrosView
from View.GraphAforadorView import GraphAforadorView
from View.InstrumentsView import InstrumentsView
from View.FormInstrumentView import FormInstrumentsView
import sys
import os

class Monitor(QMainWindow):

    data_updated_signal = pyqtSignal()
    def __init__(self):
        super(Monitor, self).__init__()
        self.setWindowTitle("Monitor N3")
        # screen_size = QDesktopWidget().screenGeometry()
        self.setGeometry(300, 130, 530, 650)
        self.setWindowIcon(QIcon("../LogoOrsep.jpg"))
        self.tabla_embalse_precipitacion = TablaEmbalseView()
        self.home_view = HomeView(self.tabla_embalse_precipitacion)

        self.create_menu()
        self.central_widget = HomeView(self.tabla_embalse_precipitacion)
        self.setCentralWidget(self.central_widget)



        self.tabla_freatimetro_view = TablaFreatimetroView()
        self.freatimeter_view = FreatimeterView(self.tabla_freatimetro_view)

        self.tabla_embalse_7piezometros = TablaPiezometrosView()
        self.piezometers_view = PiezometersView(self.tabla_embalse_7piezometros)

        self.tabla_embalse_aforadores = TablaAforadoresView()
        self.aforadores_view = AforadoresView(self.tabla_embalse_aforadores)

        self.graph_embalse_view = GraphEmbalseView()
        self.graph_freatimeter_view = GraphFreatimeterView()
        self.graph_piezometros_view = GraphPiezometrosView()
        self.graph_aforador_view = GraphAforadorView()

        self.tabla_instrumentos_view = InstrumentsView()
        self.formulario_instrumentos_view = FormInstrumentsView(self.tabla_instrumentos_view)

    def create_menu(self):
        #Menu bar
        menu_bar = self.menuBar()
        menu_inicio = menu_bar.addMenu("Inicio")
        menu_embalse = menu_bar.addMenu("Embalse")
        menu_piezometros = menu_bar.addMenu("Piezómetros")
        menu_freatimetro = menu_bar.addMenu("Freatímetros")
        menu_aforadores = menu_bar.addMenu("Aforadores")
        menu_graficos = menu_bar.addMenu("Gráficos")
        menu_instrumentos = menu_bar.addMenu("Instrumentos")

        #Acciones
        action_inicio = QAction("Inicio", self)
        action_inicio.triggered.connect(self.show_home_view)
        menu_inicio.addAction(action_inicio)

        #
        action_embalse = QAction("Embalse", self)
        action_embalse.triggered.connect(self.show_embalse_view)
        menu_embalse.addAction(action_embalse)

        action_embalse = QAction("Precipitación", self)
        action_embalse.triggered.connect(self.show_precipitacion_view)
        menu_embalse.addAction(action_embalse)

        action_embalse = QAction("Tabla", self)
        action_embalse.triggered.connect(self.show_tabla_embalse_view)
        menu_embalse.addAction(action_embalse)

        action_embalse = QAction("Gráficos", self)
        action_embalse.triggered.connect(self.show_grafico_embalse_view)
        menu_embalse.addAction(action_embalse)

        #
        action_piezometros = QAction("Medición", self)
        action_piezometros.triggered.connect(self.show_piezometros_view)
        menu_piezometros.addAction(action_piezometros)

        action_piezometros = QAction("Tabla", self)
        action_piezometros.triggered.connect(self.show_tablas_piezometros_view)
        menu_piezometros.addAction(action_piezometros)

        action_piezometros = QAction("Gráficos", self)
        action_piezometros.triggered.connect(self.show_grafico_piezometro_view)
        menu_piezometros.addAction(action_piezometros)

        #
        action_freatimetro = QAction("Medición", self)
        action_freatimetro.triggered.connect(self.show_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        action_freatimetro = QAction("Tabla", self)
        action_freatimetro.triggered.connect(self.show_tabla_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        action_freatimetro = QAction("Gráficos", self)
        action_freatimetro.triggered.connect(self.show_grafico_freatimetro_view)
        menu_freatimetro.addAction(action_freatimetro)

        #
        action_aforadores = QAction("Medición", self)
        action_aforadores.triggered.connect(self.show_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

        action_aforadores = QAction("Tabla", self)
        action_aforadores.triggered.connect(self.show_tablas_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

        action_aforadores = QAction("Gráficos", self)
        action_aforadores.triggered.connect(self.show_grafico_aforadores_view)
        menu_aforadores.addAction(action_aforadores)

        #
        action_graficos = QAction("Personalizados", self)
        action_graficos.triggered.connect(self.show_graficos_personalizados_view)
        menu_graficos.addAction(action_graficos)

        #
        action_instrumentos = QAction("Instrumentos", self)
        action_instrumentos.triggered.connect(self.show_instrumentos_view)
        menu_instrumentos.addAction(action_instrumentos)

        action_instrumentos = QAction("Agregar nuevo", self)
        action_instrumentos.triggered.connect(self.show_nuevo_instrumento_view)
        menu_instrumentos.addAction(action_instrumentos)

    def show_home_view(self):
        self.central_widget = HomeView(self.tabla_embalse_precipitacion)
        self.setCentralWidget(self.central_widget)

    def show_embalse_view(self):
        self.central_widget = EmbalseView(self.tabla_embalse_precipitacion)
        self.setCentralWidget(self.central_widget)

    def show_precipitacion_view(self):
        self.central_widget = PrecipitacionView(self.tabla_embalse_precipitacion)
        self.setCentralWidget(self.central_widget)
    def show_tabla_embalse_view(self):
        if not self.tabla_embalse_precipitacion:
            self.tabla_embalse_precipitacion = TablaEmbalseView()
        self.tabla_embalse_precipitacion.show()

    def show_grafico_embalse_view(self):
        self.graph_embalse_view.show()
    def show_piezometros_view(self):
        self.central_widget = PiezometersView(self.tabla_embalse_7piezometros)
        self.setCentralWidget(self.central_widget)

    def show_tablas_piezometros_view(self):
        if not self.tabla_embalse_7piezometros:
            self.tabla_embalse_7piezometros = TablaPiezometrosView()
        self.tabla_embalse_7piezometros.show()

    def show_grafico_piezometro_view(self):
        self.graph_piezometros_view.show()

    def show_freatimetro_view(self):
        self.central_widget = FreatimeterView(self.tabla_freatimetro_view)
        self.setCentralWidget(self.central_widget)

    def show_tabla_freatimetro_view(self):
        if not self.tabla_freatimetro_view:
            self.tabla_freatimetro_view = TablaFreatimetroView()
        self.tabla_freatimetro_view.show()

    def show_grafico_freatimetro_view(self):
        self.graph_freatimeter_view.show()

    def show_aforadores_view(self):
        self.central_widget = AforadoresView(self.tabla_embalse_aforadores)
        self.setCentralWidget(self.central_widget)

    def show_tablas_aforadores_view(self):
        if not self.tabla_embalse_aforadores:
            self.tabla_embalse_aforadores = TablaAforadoresView()
        self.tabla_embalse_aforadores.show()

    def show_grafico_aforadores_view(self):
        self.graph_aforador_view.show()
    def show_graficos_personalizados_view(self):
        pass
    def show_nuevo_instrumento_view(self):
        self.central_widget = FormInstrumentsView(self.tabla_instrumentos_view)
        self.setCentralWidget(self.central_widget)
    def show_instrumentos_view(self):
        if not self.tabla_instrumentos_view:
            self.tabla_instrumentos_view = InstrumentsView()
        self.tabla_instrumentos_view.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    fuente_path = os.path.abspath(os.path.join("..", "Fuentes", "OpenSans-Regular.ttf"))
    stylesheet_path = os.path.abspath(os.path.join("..", "Style", "style.qss"))

    # Fuente
    font_id = QFontDatabase.addApplicationFont(fuente_path)
    if font_id == -1:
        print("Error al cargar la fuente Open Sans")
    else:
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print(f"Fuente '{family}' cargada exitosamente.")

    # Stylesheet
    with open(stylesheet_path, "r") as style_file:
        app.setStyleSheet(style_file.read())

    window = Monitor()
    window.show()
    sys.exit(app.exec_())