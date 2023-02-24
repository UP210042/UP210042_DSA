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


lista=[3,0,1,5,7,9]
quicksort(lista, 0, len(lista)-1)
print(lista)             