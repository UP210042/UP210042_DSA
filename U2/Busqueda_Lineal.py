lista1=[-5,2,3,6,1,9,14]
lista2=[-3,0,5,7,9,10,14]
value=6

def lineal_Not_Sort (lista1, value):
    idx=-1 #indica que no la encontro en la lista
    pos=0
    for a in lista1:
        if a==value:
            idx=pos
            break
        pos+=1
    return idx
    
def lineal_Sort (lista2 , value):
    for b in range(len(lista2)):
        if lista2[b]== value:
         return b
        elif lista2[b]>value: #indica que no encontro el valor en la lista, saliendo de la funcion imprimiendo none
            break 
    return None    

print (lineal_Not_Sort(lista1, value))
print(lineal_Sort(lista2,value))        
    


       