#ejercicio1 
texto1 = "Python es un lenguaje poderoso"
salida = texto1.split()
npal = len(salida)
print(salida[0])
print(salida[-1])

#ejercicio 2
texto2 = "Hola    mundo  en  Python"
salida2 = " ".join(texto2.split())
print(salida2)

#ejercicio 3
texto3 = "dennys@gmail.com"
salida3 = texto3.split('@')
npal = len(salida3)
print(salida3[-1])

#ejercicio 4
texto4 = "documento.pdf"
salida4 = texto4.endswith(".pdf")
print(salida4)

#ejercicio5
texto5 = "Me gusta Python"
salida5 = " ".join(texto5.split()[::-1])
print(salida5)

#ejercicio6
solicitud = input("")
cadenasoli = solicitud.split()
poema1 = "El susurro del viento me llama, lleva tu nombre en su brisa calma. La luna brilla, cómplice del querer, en su luz veo tu alma renacer."
poema2 = "En la penumbra del recuerdo me hallo, voces lejanas cantan un triste fallo. El tiempo, verdugo sin compasión, deja cicatrices en mi corazón."
poema3 = "La noche abraza mi ser entero, un eco vacío, frío y severo. Las estrellas, mi única compañía, bailan mudas en la lejanía"
poema4 = "Del abismo oscuro logro alzarme, cada herida me enseña a levantarme. El fuego en mi pecho vuelve a encender, soy más fuerte tras cada caer"
poema5 = "Un puñal de hielo cruza el pecho, promesas rotas en un cruel despecho. Pero la verdad renace al final, un alma libre no teme el mal"

if ("amor" in cadenasoli):
    print(poema1)
elif ("melancolia" in cadenasoli):
    print(poema2)
elif ("soledad" in cadenasoli):
    print(poema3)
elif ("superacion" in cadenasoli):
    print(poema4)
elif ("traicion" in cadenasoli):
    print(poema5)
else:
    print("No hay poemas disponibles.")





