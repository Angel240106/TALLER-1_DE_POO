class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")


class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")


class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Carenado: {self.tipo_carenado}")



if __name__ == "__main__":
    coche_f1 = CocheF1("Ferrari", "SF90", 350, "Intermedios")
    moto_gp = MotoGP("Yamaha", "YZR-M1", 330, "Aerodinámico")

    print("\nInformación del coche de F1:")
    coche_f1.mostrar_info()

    print("\nInformación de la MotoGP:")
    moto_gp.mostrar_info()
