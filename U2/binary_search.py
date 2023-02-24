lista=[-3,0,1,5,7,9]
valor=6

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

x, y = binary_search (lista, valor) # Te imprime dos valores
print(x,y)