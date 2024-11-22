class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El material '{self.titulo}' ha sido prestado.")
        else:
            print(f"El material '{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El material '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El material '{self.titulo}' ya estaba disponible.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nCódigo: {self.codigo}\nEstado: {estado}")


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero):
        super().__init__(titulo, autor, codigo)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de páginas: {self.numero_paginas}\nGénero: {self.genero}")


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion):
        super().__init__(titulo, autor, codigo)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de edición: {self.numero_edicion}\nFecha de publicación: {self.fecha_publicacion}")



if __name__ == "__main__":
    libro = Libro("El Quijote", "Miguel de Cervantes", "L001", 863, "Novela")
    revista = Revista("National Geographic", "Varios", "R001", 150, "Noviembre 2024")

    print("\nInformación del libro:")
    libro.mostrar_info()

    print("\nInformación de la revista:")
    revista.mostrar_info()

    print("\nPréstamo y devolución:")
    libro.prestar()
    libro.prestar()
    libro.devolver()
    libro.devolver()
