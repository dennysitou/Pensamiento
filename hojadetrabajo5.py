#ejercicio 1 
consumo = input("Ingrese el consumo: ")
consumo = int(consumo)
habitantes = input("Ingrese el numero de habitantes de la casa: ")
habitantes = int(habitantes)

if consumo < 15:
    print(f"La tarifa es de {consumo * 5}")
elif 15 <= consumo <= 30:
    if habitantes > 3:
        print(f"La tarifa es de {consumo * 4}")
    elif habitantes == 3:
        print(f"La tarifa es de {consumo * 4}")
    else:
        print(f"La tarifa es de {consumo * 5}")
if consumo > 30:
    if habitantes > 5:
        print(f"La tarifa es de {consumo * 3.5}")
    elif habitantes % 2 == 0:
        print(f"La tarifa es de {consumo * 4}")
    else: 
        print(f"La tarifa es de {consumo * 4.2}")
        

#ejercicio 2
anio = input("Ingrese el modelo del vehiculo: ")
anio = int(anio)
placa = input("Ingrese la placa del vehiculo: ")

ultimonumero = placa[-1]
ultimonumero = int(ultimonumero)
if anio >= 2001:
    if ultimonumero % 2 == 0:
        print("El vehiculo NO puede circular los dias lunes.")
    elif ultimonumero % 2 == 1:
        print("El vehiculo NO puede circular los dias viernes.")
elif anio < 2001:
    print("El vehiculo necesita mantenimiento obligatorio.")
    if ultimonumero % 2 == 0:
        print("El vehiculo NO puede circular los dias lunes.")
    elif ultimonumero % 2 == 1:
        print("El vehiculo NO puede circular los dias viernes.")










    