import json

personas = [] 

otro = 'si'

while otro == 'si':
	persona = {}

	persona["nombre"] = input("nombre? ")
	persona["apellido"] = input("apellido: ")
	persona["dni"] = int(input("dni: "))

	personas.append(persona)
	otro = input('otro? ')

with open("personas.json", "w") as fileout:
	json.dump(personas, fileout)
