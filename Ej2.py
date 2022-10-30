contraseña1 = input("ingrese su contraseña: ")
cont = 0

contraseña2 = input("repita su contraseña: ")

if contraseña2 != contraseña1:
    for cont in range(0,2):
        contraseña2 = input("Repita su contraseña: ")
        if contraseña2 == contraseña1:
            print("Sus contraseñas coinciden")
            break
else:
    print("Sus contraseñas coinciden correctamente")