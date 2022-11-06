numero = int(input("Ingrese un número: "))

cuenta = []
while numero >= 0:
    cuenta.append(numero)
    numero = numero - 1
    # print(cuenta)

print(cuenta)