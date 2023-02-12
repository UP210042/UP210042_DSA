import random as sample

def llenar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = sample.randint(1, 1000)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def crear_matriz(tamano):
    matriz = [[0 for i in range(tamano)] for j in range(tamano)]
    matriz = llenar_matriz(matriz)
    return matriz

def main():
    tamano_matriz = int(input("Ingrese el tamaño de la matriz: "))
    matriz = crear_matriz(tamano_matriz)
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()