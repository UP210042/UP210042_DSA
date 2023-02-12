dinero_disponible = int(input("Dinero: "))
costo_boleto = 1
num_boletos = 0

while dinero_disponible >= costo_boleto:
    dinero_disponible -= costo_boleto
    num_boletos += 1
    costo_boleto += 1

print("Boletos: ", num_boletos)