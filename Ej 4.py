def mayor_comun_divisor(x,y):
    if x > y:
        menor = y
    else:
        menor = x
        for i in range(1, (menor +1)):
            if (x % i == 0) and (y % i == 0):
                mcd = i
        return mcd


divisor1 = int(input("Ingrese el primer divisor: "))
divisor2 = int(input("Ingrese el segundo divisor"))
mcd = 0

mcd = mayor_comun_divisor(divisor1, divisor2)
print(f"El MCD entre {divisor1} y {divisor2} es {mcd}")