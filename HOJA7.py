#ejercicio1
for i in range(1,11):
     if i % 2 == 1:
         print(i)
         
#ejercicio2
x = 1 
while x < 11:
    if x % 2 == 1:
        print(x)
    x += 1

#escenario1 
while True:
    palabra = input("Ingrese una palabra secreta: ")
    if palabra == "chupacabra":
        print("Has dejado el bucle con exito.")
        break
    
#escenario2
palabra1 = input("Ingresa una palabra:")

palabra1 = palabra1.upper()

for letra in palabra1:
    if letra in 'AEIOU':
        continue
    print(letra)
    
        