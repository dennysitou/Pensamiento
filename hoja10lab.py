#clinica
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def mostrar_datos_medicos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
    
    def calcular_dosis(self):
        return self.peso * 0.1
    
    def generar_ficha_medica(self):
        print("\n--- Ficha Médica ---")
        self.mostrar_datos_medicos()
        print(f"Dosis recomendada: {self.calcular_dosis():.2f} mg")


class Perro(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso)
        self.raza = input("Raza del perro: ")
        self.vacunado = input("Está vacunado?").lower() == "sí"
    
    def calcular_dosis(self):
        return super().calcular_dosis() * 1.2
    
    def generar_ficha_medica(self):
        super().generar_ficha_medica()
        print(f"Raza: {self.raza}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")


class Gato(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso)
        self.pelaje = input("Tipo de pelaje: ")
        self.esterilizado = input("Está esterilizado? ").lower() == "sí"
    
    def calcular_dosis(self):
        return super().calcular_dosis() * 0.85
    
    def generar_ficha_medica(self):
        super().generar_ficha_medica()
        print(f"Tipo de pelaje: {self.pelaje}")
        print(f"Esterilizado: {'Sí' if self.esterilizado else 'No'}")


class Ave(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso)
        self.especie = input("Especie del ave: ")
        self.puede_volar = input("Puede volar? ").lower() == "sí"
    
    def calcular_dosis(self):
        return super().calcular_dosis() * 0.7
    
    def generar_ficha_medica(self):
        super().generar_ficha_medica()
        print(f"Especie: {self.especie}")
        print(f"Puede volar: {'Sí' if self.puede_volar else 'No'}")


class Reptil(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso)
        self.tipo_reptil = input("Tipo de reptil: ")
        self.venenoso = input("Es venenoso?").lower() == "sí"
    
    def calcular_dosis(self):
        return super().calcular_dosis() * 0.5
    
    def generar_ficha_medica(self):
        super().generar_ficha_medica()
        print(f"Tipo de reptil: {self.tipo_reptil}")
        print(f"Venenoso: {'Sí' if self.venenoso else 'No'}")


def crear_animal():
    print("\nTipos de animales disponibles:")
    print("1. Perro\n2. Gato\n3. Ave\n4. Reptil")
    
    tipo = input("Seleccione el tipo de animal (1-4): ")
    
    nombre = input("Nombre del animal: ")
    edad = int(input("Edad (años): "))
    peso = float(input("Peso (kg): "))
    
    if tipo == "1":
        return Perro(nombre, edad, peso)
    elif tipo == "2":
        return Gato(nombre, edad, peso)
    elif tipo == "3":
        return Ave(nombre, edad, peso)
    elif tipo == "4":
        return Reptil(nombre, edad, peso)
    else:
        print("Opción no válida")
        return None

animales = []

while True:
    print("Menú:")
    print("1. Registrar nuevo animal")
    print("2. Mostrar fichas médicas")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        animal = crear_animal()
        if animal:
            animales.append(animal)
            print("Animal registrado con exito")
    elif opcion == "2":
        if not animales:
            print("No hay animales registrados.")
        else:
            for animal in animales:
                animal.generar_ficha_medica()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no valida.")
    
    
    
#personas en institucion
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"DNI: {self.dni}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.carrera = input("Carrera que estudia: ")
        self.semestre = int(input("Semestre: "))
        self.promedio = float(input("Promedio académico: "))
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo: Estudiante")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio: {self.promedio}")


class Profesor(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.departamento = input("Departamento: ")
        self.especialidad = input("Especialidad: ")
        self.años_experiencia = int(input("Años de experiencia: "))
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo: Profesor")
        print(f"Departamento: {self.departamento}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Años de experiencia: {self.años_experiencia}")


class Administrativo(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.puesto = input("Puesto: ")
        self.area = input("Area: ")
        self.antiguedad = int(input("Antiguedad en años: "))
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo: Administrativo")
        print(f"Puesto: {self.puesto}")
        print(f"Área: {self.area}")
        print(f"Antigüedad: {self.antiguedad} años")


def crear_persona():
    print("Tipos de personas:")
    print("1. Estudiante\n2. Profesor\n3. Administrativo")
    
    tipo = input("Seleccione el tipo de persona (del 1 al 3): ")
    
    nombre = input("Nombre completo: ")
    edad = int(input("Edad: "))
    dni = input("Identificacion: ")
    
    if tipo == "1":
        return Estudiante(nombre, edad, dni)
    elif tipo == "2":
        return Profesor(nombre, edad, dni)
    elif tipo == "3":
        return Administrativo(nombre, edad, dni)
    else:
        print("Opción no válida")
        return None

personas = []

while True:
    print("Menu:")
    print("1. Registrar nueva persona")
    print("2. Mostrar información de personas")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        persona = crear_persona()
        if persona:
            personas.append(persona)
            print("Persona registrada con exito")
    elif opcion == "2":
        if not personas:
            print("No hay personas registradas")
        else:
            for persona in personas:
                persona.mostrar_informacion()
                print("-" * 30)
    elif opcion == "3":
        print("Saliendo del sistema")
        break
    else:
        print("Opcion no valida")