numero1 = int(input(" ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))
operacion = input("Operacion S)uma R)esta M)ultiplicacion D)ivision: ")

if operacion == "S":
    print("El resultado de la suma es: " + str(numero1 + numero2))
elif operacion == "R":
    print("El resultado de la resta es: " + str(numero1 - numero2))
elif operacion == "M":
    print("El resultado de la multiplicacion es: " + str(numero1 * numero2))
else:
    print("el resultado de la division es: " + str(numero1 / numero2))
