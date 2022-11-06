meses = int(input("Ingrese la cantidad de meses: "))
adultos = 2
recien_nacidas = 0
parejas = 1
for i in range(0, (meses+1)):
    parejas = adultos // 2                         #Esta division entera para saber cuantas parejas de adultos tenemos y por cada pareja de adultos se genera una nueva recien nacido
    adultos = adultos + recien_nacidas
    recien_nacidas = parejas
    # print(f"{parejas}, {adultos}, {recien_nacidas}")

print(f"En {meses} meses a partir de una pareja de adultos, obtendra:"
      f"\nParejas Adultas: {parejas}\nAdultos: {adultos}\nRecien Nacidos: {recien_nacidas}")