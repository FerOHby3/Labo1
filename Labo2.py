print("Matriz de Operaciones\n")

numcol=int(input("Ingrese la cantidad de columnas que quiere "))
numfil=int(input("Ingrese la cantidad de filas que quiere "))

matriz = [["" for _ in range(numcol)] for _ in range(numfil)]

def imp_matriz(matriz):
    for fila in matriz:
        for asiento in fila:
            print(asiento, end=" ")
        print()

def asiento_disp():
    for a in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[a][y] == "":
                return a, y
espacios = numcol*numfil

while espacios > 0:
    imp_matriz(matriz)
    fila = int(input("Elija la fila del asiento (0-6): "))
    columna = int(input("Elija la columna del asiento (0-5): "))
        
    if matriz[fila][columna] == "":
        matriz[fila][columna] = input("Ingrese numero para rellenar ")
        espacios -= 1

    else:
        print("El asiento ya ha sido ocupado")
        print("Sugerimos el asiento")
        asienton = asiento_disp()
        if asienton:
            fila, columna = asienton
            print("Fila: {}, Columna: {}".format(fila, columna))
    respuesta=""
