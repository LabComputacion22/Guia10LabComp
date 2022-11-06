barras_novendidas = int(input("Ingrese la cantidad de barras de pan que no son del dia: "))

precio_barra = 3.49
descuento = 0.60
precio_final = (barras_novendidas * precio_barra * descuento)

print(f"Usted tiene {barras_novendidas} barras de pan no frescas.\nPrecio regular por barra es de: {precio_barra}"
      f"\nEl descuento a las barras de pan no frescas es de 60% "
      f"\nEl precio final de sus barras de pan no frescas es de: {precio_final}")