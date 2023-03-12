lista=[5,2,1,6,3,4,7,9]
a = []
vuelta=2
for i in range(vuelta):
    a=lista.pop()
    lista.insert(0, a)   
print(lista, end=" ")