#ejercicio1 
tam = int(input("ingresa el tamaño del arreglo: "))
base = int(input("ingrese la base: "))

def multiplos(tam, base):
    arreglo = []
    for i in range(1, tam + 1):
        arreglo.append(base * i)
    return arreglo

arreglo1 = multiplos(tam, base)

print(arreglo1)

#ejercicio2
tamaño = int(input("Ingresa el tamaño de los vectores: "))

nombres = []
longitudes = []

for i in range(tamaño):
    nombre = input(f"Ingresa el nombre de la persona {i + 1}: ")
    nombres.append(nombre)
    longitudes.append(len(nombre))

print(nombres)
print(longitudes)

#escenario1
opciones = ["1. Malo", "2. Regular", "3. Buena", "4. Muy Buena", "5. Excelente"]

atencion = []
conteo_respuestas = [0, 0, 0, 0, 0]

clientes = int(input("Ingrese la cantidad de clientes atendidos: "))

for i in range(clientes):
    print("Opciones:", opciones)
    print("Ingrese la respuesta del cliente", i + 1)
    respuesta = int(input())
    if 1 <= respuesta <= 5:
        atencion.append(respuesta)
        conteo_respuestas[respuesta - 1] += 1
    else:
        print("Opción no válida. Intente nuevamente.")
        break

tipos_respuestas = ["Malo", "Regular", "Buena", "Muy Buena", "Excelente"]
print("Total de respuestas por tipo:")
for i in range(5):
    print(tipos_respuestas[i], ":", conteo_respuestas[i])

respuesta_mas_frecuente = tipos_respuestas[conteo_respuestas.index(max(conteo_respuestas))]
print("La respuesta más frecuente es", respuesta_mas_frecuente)

promedio = sum(atencion) / len(atencion)
print("Promedio:", promedio)

clientes_menores_al_promedio = []
for i in range(len(atencion)):
    if atencion[i] < promedio:
        clientes_menores_al_promedio.append(i + 1)

print("Clientes con respuestas menores al promedio:", clientes_menores_al_promedio)
print("Porcentaje menor al promedio:", (len(clientes_menores_al_promedio) / clientes) * 100)
