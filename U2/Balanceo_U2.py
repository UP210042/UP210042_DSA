cadena = input("Introduce una cadena de paréntesis: ")
abiertos = 0
for caracter in cadena:
    if caracter == "(":
        abiertos += 1
    elif caracter == ")":
        abiertos -= 1
        if abiertos < 0:
            print("La cadena no está balanceada.")
            break
if abiertos == 0:
    print("La cadena está balanceada.")
elif abiertos > 0:
    print("La cadena no está balanceada.")