saldo_actual = 3000
intentos = 3

while True:
    print(f"Saldo actual: {saldo_actual}")
    retirada = int(input("Ingrese el monto a retirar (o 0 para salir): "))

    if retirada == 0:
        print("Operación cancelada. Adios.")
        break

    if retirada > saldo_actual:
        intentos -= 1
        print(f"Saldo insuficiente. Intentos restantes: {intentos}")
        if intentos == 0:
            print("Los intentos llegaron a su limite. Cuenta bloqueada.")
            break
    else:
        saldo_actual -= retirada
        print(f"Retiro exitoso. Nuevo saldo: {saldo_actual}")
        if saldo_actual == 0:
            print("Saldo agotado. Adios.")
            break