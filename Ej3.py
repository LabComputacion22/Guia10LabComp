def costo_llamada(tarifa, minutos):
    coste = (tarifa * minutos)
    return coste
    # print(costo)


minutos = float(input("Ingrese los minutos hablados"))
pais = input("Ingrese el pais desde donde realizo la llamada").lower()
tarifa = float(input("Ingrese la tarifa la llamada en euros"))
costo = 0

costo = costo_llamada(tarifa, minutos)
print(f"El costo de la llamada de {minutos} minutos, desde {pais}, con una tarifa de {tarifa} euros es de {costo} euros")
