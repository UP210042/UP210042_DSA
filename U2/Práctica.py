import random
# Generas los 100 numeros dentro del rango 101-500
L=[random.randint(101, 500)] #este es L[0]
i=1
while i<100:
  numerito=random.randint(101,500)          # mientras este dentro del ciclo while, genera numeros que no se repiten
  for j in range(0, len(L)):                # utilizando el contador para ir aumentando los valores
    if L[j]==numerito:
      break
  else:
    L.append(numerito)
    i+=1
# Bubble sort
def Bubble_Sort(numerito): 
    for i in range(0, len(numerito)+1 -2):
        for j in range(0,len(numerito)+1 - i-2):
            x = numerito[j]
            y = numerito[j+1]
            if x > y:
                numerito[j] = y
                numerito[j+1] = x
    return numerito            
# Matriz // ordena los valores dentro de una matriz de 10x10
def matricita(matriz,L):
    matriz=[[0 for j in range (10)]for i in range (10)]
    indice=0
    for i in range (10):
        for j in range (10):
            matriz[i][j]=L[indice]
            indice += 1
    return matriz        
# Utilizas el binary search para encontrar el valor
def binary_search(lista, valor):
    principio=0
    final=len(lista)-1
    mitad=((principio+final)//2)
    i=0
    while principio<=final and lista[mitad]!=valor:
        if valor < lista[mitad]:
            final=mitad-1
        else:
            principio=mitad+1
        mitad=((principio+final)//2)
        i+=1
    if lista[mitad] == valor:
        lugar=mitad
    else:
        lugar=-1        
    return lugar, i
# Quick sort
def quicksort (a,primero,ultimo):
    central=(primero+ultimo)//2
    pivote=a[central]
    i=primero
    j=ultimo
    while i<=j: 
        while a[i]<pivote:
            i+=1
        while a[j]>pivote:
            j-=1
        if i<=j:
            a[i], a[j] = a[j], a[i]
            i+=1
            j-=1
    if primero<j:
        quicksort(a,primero,j)
    elif i<ultimo:
        quicksort(a,i,ultimo)      

# Resultados
matriz=[]; valor=404
Bubble_Sort(L)
for i in matricita(matriz, L):
    print(i)
x, y = binary_search (L, valor) # Te imprime dos valores
print(x,y)
quicksort(L, 0, len(L)-1)
print(L)  