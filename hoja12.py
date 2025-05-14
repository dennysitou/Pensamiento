dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Ingrese los niveles de presión de lunes a domingo: ")
nv3 = [int(valor) for valor in input().split()]

print("-----------Sistolica------------")
if len(nv3) != 7:
    print("Error: Debes ingresar exactamente 7 valores")
else:
    for i in range(7): #sistolica
        if nv3[i] < 120:
            print(dias[i], ": Normal")
        elif 120 <= nv3[i] <= 129:
            print(dias[i], ": Elevada")
        elif 130 <= nv3[i] <= 139:
            print(dias[i], ": Hipertensión Etapa 1")
        else:
            print(dias[i], ": Hipertensión Etapa 2")
            
print ("-----------Diastolica-----------")
for i in range(7): #diastolica
        if nv3[i] < 80:
            print(dias[i], ": Normal")
        elif 80 < nv3[i]:
            print(dias[i], ": Elevada")
        elif 80 <= nv3[i] <= 89:
            print(dias[i], ": Hipertensión Etapa 1")
        else:
            print(dias[i], ": Hipertensión Etapa 2")