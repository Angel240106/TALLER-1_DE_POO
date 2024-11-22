import math

class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado.")
        return None


class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        volumen = self.lado ** 3
        return volumen

    def mostrar_info(self):
        print(f"Cubo: Lado = {self.lado}")
        print(f"Volumen = {self.calcular_volumen():.2f}")


class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return volumen

    def mostrar_info(self):
        print(f"Esfera: Radio = {self.radio}")
        print(f"Volumen = {self.calcular_volumen():.2f}")



if __name__ == "__main__":
    cubo = Cubo(3)
    esfera = Esfera(5)

    print("\nInformación del cubo:")
    cubo.mostrar_info()

    print("\nInformación de la esfera:")
    esfera.mostrar_info()

