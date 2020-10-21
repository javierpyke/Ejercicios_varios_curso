"""Desarrollar la función cargarLstAlu que retorne una lista de los datos de alumnos
	( lista de lista ). Por cada alumno se cargará una lista con DNI, nombre y edad ( una lista
	por cada alumno ). El listado general con los datos de alumnos se almacenará en una
	única lista. Por tanto se tendrá una lista conteniendo un grupo de listas ( lista de lista ).
	Ejemplo:
	[[2698705, 'James Howlett', 18], [38698705, 'Aurora Monroe', 22],[35698705, 'Jean Grey', 22]]
	Desarrollar la función ordenarAluXDNI que reciba por parámetro la lista generada en
	cargarAlu y la ordene en forma descendente por DNI.
	Desde el programa principal invocar a cargarAlu donde se cargará la lista de datos de
	los alumnos. Una vez terminada la carga imprimir la lista por pantalla. Luego invocar a
	ordenarAluxDNI , que ordenará la lista por DNI. A continuación volver a imprimir la lista
	para verificar que su orden sea el correcto."""

def cargarAlu():
    dni=int(input("Ingrese el DNI del alumno: "))
    if dni == 0:
        return []
    else:
        nombre=str(input("Ingrese el nombre del alumno: "))
        edad=int(input("Ingrese la edad del alumno: "))
        return [dni,nombre,edad]

def cargarLstAlu():
    alumnos=[]
    alumno=cargarAlu()
    while len(alumno) != 0:
        alumnos.append(alumno)
        alumno=cargarAlu()
    return alumnos                

def ordenarAluxDNI(alumnos):
    for i in range(0, len(alumnos) - 1):
        for d in range((i+1), len(alumnos)):
            if alumnos[i][0] >= alumnos[d][0]:
                aux = alumnos[i]
                alumnos[i] = alumnos[d]
                alumnos[d] = aux
    return alumnos

def main():
    alumnos=cargarLstAlu()
    print("Los alumnos son: ",alumnos)
    ordenarAluxDNI(alumnos)
    print("La lista ordenada de alumnos es: ",alumnos)


main()