# Unit 1
### Certification evidence

[Python_Essentials_1_Badge20230209-28-1trn736.pdf](https://github.com/UP210042/UP210042_DSA/files/10698736/Python_Essentials_1_Badge20230209-28-1trn736.pdf)

Here there are the 6 works that the teacher said to us that qe need to do:

# 1.- Bisection   
```
def samesign(a, b):
        return a * b > 0
def biseccion(funcion, bajo, alto):
    assert not samesign(funcion(bajo), funcion(alto)) # una asercion permite que se encuentre una causa raiz probable de un error mas rapido
    for i in range(54):
        puntomedio = (bajo+alto) / 2.0
        if samesign(funcion(bajo), funcion(puntomedio)):
            bajo= puntomedio
        else:
            alto = puntomedio
    return puntomedio
def f(x):
        return -26+85*x-91*x**2+44*x**3-8*x**4+ x**5
x = biseccion(f, 0, 1)
print(x, f(x))
```
### Demostration:


# 2.- Secret number
```
import random
intentos=0
numero=random.randint(1,1000) 
while intentos<numero:
    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
    estimacion=input()
    estimacion=int(estimacion)
    intentos+=1
    if estimacion<numero:
        print("you're far away!")
    if estimacion>numero:
        print("you're near!")    
    if estimacion==numero:
        break
if estimacion==numero:  
    intentos=str(intentos)    
    print("You did it! in only : " + intentos + " attempts!")
```
### Demostration:


# 3.- Tickets
```
dinero_disponible = int(input("Dinero: "))
costo_boleto = 1
num_boletos = 0

while dinero_disponible >= costo_boleto:
    dinero_disponible -= costo_boleto
    num_boletos += 1
    costo_boleto += 1

print("Boletos: ", num_boletos)
```
### Demostration:


# 4.- Bubble:

```
a = [5,2,7,9,3]

for i in range(0, len(a)):
    print(a[i])

# Bubble sort
for i in range(0, len(a)+1 -2):
    for j in range(0,len(a)+1 - i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x

print(a)        
```

### Demostration:


# 5.- Matriz No Repeat:

```
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
```

### Demostration:


# 6.- Palindromo:

```
def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida

def determinar_palindromo():
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print("Es palindromo")
    else:
        print("No es palindromo")   

if __name__ == "__main__":
    determinar_palindromo()
```
### Demostration:
