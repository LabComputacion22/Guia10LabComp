numerador = int(input("Ingrese el numerador: "))
denominador = int(input("Ingrese el denominador: "))

num1 = numerador
num2 = denominador
resto_ant = 1
resto = 1

while resto != 0:
    resto = num1 % num2
    num1 = num2
    num2 = resto
    if resto != 0:                           # Este if es para no perder el ultimo resto antes de que se haga 0
        resto_ant = resto
    # print(f"{resto}, {resto_ant}")

print(f"El C.M.D. entre {numerador} y {denominador} es {resto_ant}")