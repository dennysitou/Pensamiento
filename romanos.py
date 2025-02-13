num = int(input("Ingrese un número del 1 al 9: "))

if 1 <= num <= 9:
    romano = "I" * (num % 5)
    if num == 4:
        romano = "IV"
    elif num >= 5:
        romano = "V" + "I" * (num - 5)
    print(romano)
else:
    print("Número fuera de rango")