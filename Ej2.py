contraseña1 = input("ingrese su contraseña")
cont = 0

contraseña2 = input("repita su contraseña")

if contraseña2 != contraseña1:
    cont = 0
    while (cont < 4) or (contraseña2 != contraseña1):
        contraseña2 = input("Repita su contraseña")
        if contraseña2 == contraseña1:
            print("Sus contraseñas coinciden")
        else:
            cont = cont + 1
else:
    print("Sus contraseñas coinciden correctamente")