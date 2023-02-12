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