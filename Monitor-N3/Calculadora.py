import math
class Calculadora:
    def calcular_np(self, cb, lectura, angulo):
        return (cb-((-math.cos(angulo))*lectura))

    def calcular_caudal(self, volumen, tiempo):
        return (volumen/tiempo)

    def calcular_caudal_parshall(self, ha, k, u):
        return (k*(ha**u))