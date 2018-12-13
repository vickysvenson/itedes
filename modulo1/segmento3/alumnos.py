def agregarAlumno(alumnos):
	alumno = {}
	alumno['dni'] = int(input('Ingrese DNI: '))
	alumno['nombre'] = input('Ingrese nombre: ')
	alumno['apellido'] = input('Ingrese apellido: ')
	alumno['fecha'] = input('Ingrese fecha de nacimiento: ')
	alumno['direccion'] = input('Ingrese direccion: ')
	alumno['telefono'] = int(input('Ingrese numero de telefono: '))
	alumno['email'] = input('Ingrese su email: ')
	alumnos.append(alumno)

	return alumnos


def listarAlumnos(alumnos):
	for alumno in alumnos:
		print('DNI: ' + str(alumno['dni']))
		print('nombre: ' + alumno['nombre'])
		print('Apellido: ' + alumno['apellido'])
		print('fecha de nacimiento: ' + str(alumno['fecha']))
		print('direccion: ' + alumno['direccion'])
		print('telefono: ' + str(alumno['telefono']))
		print('email: ' + alumno['email'])
		print()


# MAIN

alumnos = []

opcion = -1

while opcion != 0:
	print('================')
	print('     Menu       ')
	print('================')
	print('1 Agregar alumno')
	print('2 Listar alumnos')
	print('0 Salir')
	print()
	opcion = int(input('Seleccione la Opcion deseada: '))
	print()
	if opcion == 1:
		alumnos = agregarAlumno(alumnos)
		print()
	elif opcion == 2:
		listarAlumnos(alumnos)
		print()
	elif opcion == 0:
		print('Chau!')
	else:
	print('Opcion incorrecta')
