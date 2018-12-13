import json 

persona = {}

with open('persona.json' , 'r') as fin:
	persona = json.load(fin)

print(persona)

