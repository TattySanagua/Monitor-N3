import math
class Calculadora:
    def calcular_np(self, cb, lectura):
        return (cb-((-math.cos(180))*lectura))

    def calcular_caudal(self, volumen, tiempo):
        return (volumen/tiempo)