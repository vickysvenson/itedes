def agregarPersona(personas):
	persona = {}
	persona["nombre"] = input("ingrese su nombre: ")
	persona["apellido"] = input("ingrese su apellido: ")

	comidas = []

	otraComida = 'si'

	while otraComida == 'si':
		comidas.append(input('ingrese comida favorita: '))

		otraComida = input('Desea agregar otra comida (si/no)? ')

	persona["comidas"] = comidas

	personas.append(persona)

	return personas
	

def listarPersonas(personas):
	for persona in personas:
		print("Nombre: " + persona["nombre"])
		print("apellido: " + persona["apellido"])
		print("comida favorita: " + str(persona["comidas"]))



#MAIN

personas = []
opcion = -1

while opcion != 0:
	print ("==================")
	print ("    OPCIONES      ")
	print ("==================")
	print ()
	print ("1 agregar personas")
	print ("2 listar")
	print ("0 salir")
	print()
	opcion = int(input("seleccione la opcion deseada: "))
	if opcion == 1:
		personas = agregarPersona(personas)
		print()
	elif opcion == 2:
		listarPersonas(personas)
		print()
	elif opcion == 0:
		print("chau!")
	else: 
		print("Opcion Incorrecta")



