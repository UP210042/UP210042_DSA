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