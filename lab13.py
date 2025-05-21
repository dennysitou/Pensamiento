def siguiente_generacion(matriz):
    matriz= [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    ]
    
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    nuevamatriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            vecinos = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    ni, nj = i + x, j + y 
                    if 0 <= ni < filas and 0 <= nj < columnas:
                        vecinos += matriz[ni][nj]
                    
            celda_actual = matriz[i][j]
            
            vecinos_lr = 0
            if j > 0:
                vecinos_lr += matriz[i][j-1]  
            if j < columnas - 1:
                vecinos_lr += matriz[i][j+1] 
                
            if celda_actual == 1:
                if vecinos_lr == 1 or vecinos_lr == 2:
                    nuevamatriz[i][j] = 1  
                else:
                    nuevamatriz[i][j] = 0  
            
            else:
                if vecinos_lr == 1:
                    nuevamatriz[i][j] = 1 
                else:
                    nuevamatriz[i][j] = 0  
    
    return nuevamatriz

def imprimir_tablero(matriz):
    for fila in matriz:
        print(' '.join(str(celda) for celda in fila))
    print()

matriz = [ 
    [0,0,0,0,0,0,0,1,1,0], 
    [0,1,1,0,0,0,0,0,0,0], 
    [0,1,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,1,1,0,0,0], 
    [0,0,0,0,0,1,1,0,0,0], 
    [0,0,1,1,0,0,0,0,0,0], 
    [0,0,1,1,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,1,0], 
] 

print("Generacion 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("Generacion 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("Generacion 2:")
imprimir_tablero(generacion_2)

            
