class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Especie: {self.especie}")


class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    def ladrar(self):
        print("Guau, guau")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")


class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad, "Gato")
        self.color = color

    def maullar(self):
        print("Miau")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")


# Ejemplo de uso
if __name__ == "__main__":
    perro = Perro("Max", 3, "Golden Retriever")
    gato = Gato("Luna", 2, "Negro")

    print("\nInformación del perro:")
    perro.mostrar_info()
    perro.ladrar()

    print("\nInformación del gato:")
    gato.mostrar_info()
    gato.maullar()
