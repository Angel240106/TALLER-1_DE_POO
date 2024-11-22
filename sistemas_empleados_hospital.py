class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario Base: ${self.salario_base:,.2f}")


class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")
        print(f"Número de pacientes atendidos: {self.num_pacientes}")


class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Turno: {self.turno}")
        print(f"Planta: {self.planta}")



if __name__ == "__main__":
    medico = Medico("Dr. Juan Pérez", "M001", "Cardiología", 75000, "Cardiología", 120)
    enfermero = Enfermero("Ana López", "E001", "Pediatría", 45000, "Noche", 3)

    print("\nInformación del médico:")
    medico.mostrar_info()

    print("\nInformación del enfermero:")
    enfermero.mostrar_info()
