import json
persona = {}
persona['nombre'] = input("nombre: ")
persona['apellido'] = input("apellido: ")

with open('persona.json', 'w')as fout:
		json.dump(persona, fout)
