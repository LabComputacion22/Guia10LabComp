objetivo = int(input("Ingrese la cantidad objetivo de ahorro: "))
ahorro = int(input("Ingrese la cantidad de dinero que ahorra: "))
acumulado = 0

while acumulado < objetivo:
    acumulado = (acumulado + ahorro)
    if acumulado < objetivo:

        ahorro = int(input("Ingrese la cantidad de dinero que ahorra: "))
    else:
        break