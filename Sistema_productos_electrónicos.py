class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Marca: {self.marca}")


class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de batería: {self.capacidad_bateria} mAh")


class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño de pantalla: {self.tamano_pantalla} pulgadas")



if __name__ == "__main__":
    telefono = TelefonoMovil("iPhone 14", 999.99, "Apple", 4323)
    laptop = Laptop("MacBook Pro", 1999.99, "Apple", 16)

    print("\nInformación del teléfono móvil:")
    telefono.mostrar_info()

    print("\nInformación de la laptop:")
    laptop.mostrar_info()
