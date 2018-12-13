agregarOtro = "si"

listaSuper = []

while agregarOtro == "si":

    listaSuper.append(input("Ingrese producto a comprar: "))
    print()

    agregarOtro = input("desea agregar otro producto? (si/no): ")
    print()
for producto in listaSuper:
    print(producto)
