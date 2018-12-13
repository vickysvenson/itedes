def generarBaseDatos():
    listaPalabras = []

    continuar = "si"
    
    while continuar == "si":
        listaPalabras.append(input("Ingrese una palabra: "))
    

        continuar=input("Desea agregar otra palabra? (si/no): ")
        

    return listaPalabras



def buscarPalabraAleat(listaPalabras):
    import random
    palabraAleatoria = random.randint(0, len(listaPalabras) -1)
    return listaPalabras[palabraAleatoria]


# MAIN ESTO ES EL PROGRAMA
print()
print("**********AQUI COMIENZA EL JUEGO********")
print()


miLista = generarBaseDatos()
miPalabra = buscarPalabraAleat(miLista)


print()
print("============================")
print("la palabra elegida es ......")
print("============================")
print()

palabra=list(miPalabra)

vidas=6
faltan=len(palabra)
mostrarPalabra=[]

print()

for i in range(len(palabra)):
    mostrarPalabra.append('*')

while vidas > 0 and faltan > 0:
    print(mostrarPalabra)
    letra = input("Ingrese una letra: ")

    if letra in palabra:
        faltan = faltan - palabra.count(letra)
        print("letras restantes: ", faltan)

        for i in range(len(palabra)):
            if palabra[i] == letra:
                mostrarPalabra[i] = letra

    else:
        vidas= vidas-1
        print("vidas: ", vidas)

if faltan ==0:
    print("Ganaste el juego!!!!!!")
    print("la palabra es ", palabra)

elif vidas ==0:
    print("Perdiste,podes intentarlo nuevamente!!!")


        





   

