class OperacionCientifica:
    def calcular(self):

class RaizCuadrada(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero
    
    def calcular(self):
        if self.numero < 0:
        return self.numero ** 0.5

class Potencia(OperacionCientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente
    
    def calcular(self):
        return self.base ** self.exponente

class Logaritmo(OperacionCientifica):
    def __init__(self, numero, base=10):
        self.numero = numero
        self.base = base
    
    def calcular(self):
        if self.numero <= 0:
        if self.base <= 0 or self.base == 1:
            raise ValueError("La base del logaritmo debe ser positiva y diferente de 1")
        
        # Aproximación de logaritmo sin math.log
        epsilon = 1e-10
        resultado = 0
        x = self.numero
        
        while x < 1:
            x *= self.base
            resultado -= 1
        
        while x >= self.base:
            x /= self.base
            resultado += 1
        
        suma = 1
        termino = 1
        n = 1
        
        while termino > epsilon:
            termino = ((x - 1) / (x + 1)) ** (2 * n - 1) / (2 * n - 1)
            suma += termino
            n += 1
        
        return resultado + 2 * suma

class Factorial(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero
    
    def calcular(self):
        if not isinstance(self.numero, int) or self.numero < 0:
            raise ValueError("El factorial solo está definido para enteros no negativos")
        
        resultado = 1
        for i in range(1, self.numero + 1):
            resultado *= i
        return resultado

def menu_calculadora():
    print("\nCalculadora Científica Personalizada")
    print("1. Raíz cuadrada")
    print("2. Potencia")
    print("3. Logaritmo")
    print("4. Factorial")
    print("5. Salir")
    
    try:
        opcion = int(input("Seleccione una operación (1-5): "))
        return opcion
    except ValueError:
        print("Error: Ingrese un número válido")
        return None

# Programa principal
while True:
    opcion = menu_calculadora()
    
    if opcion is None:
        continue
    elif opcion == 1:
        try:
            num = float(input("Ingrese el número para calcular su raíz cuadrada: "))
            operacion = RaizCuadrada(num)
            resultado = operacion.calcular()
            print(f"La raíz cuadrada de {num} es: {resultado:.4f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif opcion == 2:
        try:
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            operacion = Potencia(base, exponente)
            resultado = operacion.calcular()
            print(f"{base} elevado a {exponente} es: {resultado:.4f}")
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
    elif opcion == 3:
        try:
            num = float(input("Ingrese el número para calcular el logaritmo: "))
            base = input("Ingrese la base del logaritmo (10 por defecto): ")
            base = float(base) if base else 10
            operacion = Logaritmo(num, base)
            resultado = operacion.calcular()
            print(f"Logaritmo base {base} de {num} es: {resultado:.4f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif opcion == 4:
        try:
            num = int(input("Ingrese un número entero para calcular su factorial: "))
            operacion = Factorial(num)
            resultado = operacion.calcular()
            print(f"El factorial de {num} es: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
    elif opcion == 5:
        print("Saliendo de la calculadora...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")