alumnos = []
continuar = "si"
while continuar == "si":
    alumno = {}
    alumno["dni"]= input("dni: ")
    alumno["nombre"]= input("nombre: ")

    alumnos.append(alumno)
    continuar = input("continuar: ")
print(alumnos)
