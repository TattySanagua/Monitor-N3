import math
class Calculadora:
    def calcular_np(self, cb, lectura):
        return (cb-((-math.cos(180))*lectura))

    def calcular_caudal(self, volumen, tiempo):
        return (volumen/tiempo)

    def calcular_caudal_parshall(self, ha):
        return (0.1771*(ha**1.55))