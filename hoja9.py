#1
def es_paroimpar(n):
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

#2
def sumalista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumalista(lista[1:])

#3
def cuentar(n):
    if n < 0:
        print("¡Despegue!")
    else:
        print(n)
        cuentar(n - 1)

#4
def cuentaas(n, actual=1):
    if actual > n:
        return
    else:
        print(actual)
        cuentaas(n, actual + 1)

#5
def sumahasta(n):
    if n <= 0:
        return 0
    else:
        return n + sumahasta(n - 1)

#6
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)

#7
def min(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        menor_del_resto = min(lista[1:])
        return lista[0] if lista[0] < menor_del_resto else menor_del_resto

#juego
import time

def adivina_el_numero(numero, intentos, tiempo_inicio):
    if intentos == 0:
        print("El número era:", numero)
        return
    intento = int(input("Tu intento: "))
    if intento == numero:
        tiempo_total = time.time() - tiempo_inicio
        print("Adivinaste!")
        print(f"Tiempo: {tiempo_total} sgs")
    elif intento < numero:
        print("El numero es mayor")
        adivina_el_numero(numero, intentos - 1, tiempo_inicio)
    else:
        print("El numero es menor")
        adivina_el_numero(numero, intentos - 1, tiempo_inicio)

