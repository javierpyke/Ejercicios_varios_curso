"""Desarrollar la función agregar que retorne una lista con los datos de alumnos cargados 
	desde el teclado. Por cada alumno se cargará una tupla con el DNI.
	Para cada DNI se le asignará una lista con: una sublista con el apellido, nombre y
	otra sublista con las notas obtenidas. Por tanto se tendrá una lista de tuplas como el
	siguiente ejemplo:
	
	[(2698705,[['Juan','Perez'],[2,9,7]]),(38698705,[['Aurora','Blancasi'],[9,9,9]]),(35698705,
										[['Raul','Grey'],[2,2,7]])]
	
	Desarrollar la función imprimirc que recibe por parámetro la lista de alumnos, la función
	deberá imprimir la lista en el orden que fue cargada.
	Desarrollar la función impirmirOrd que recibe por parámetro la lista de alumnos, la
	función deberá imprimir la lista de alumnos ordenada por dni.
	
	Desde el programa principal invocar agregar para la carga de la lista,
	luego imprimir la lista tal cual fue cargada invocando a imprimir y por último
	volver a imprimir la lista pero esta vez en forma ordenada invocando a
	impirmirOrd."""

def obtener_notas():
    notas=[]
    nota=int(input("Ingrese una nota: "))
    while nota != -1:
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            nota=int(input("Ingrese una nota: "))
        else:
            print("Nota invalida.")
            nota=int(input("Ingrese una nota: "))
    return notas

def obtener_alumno():
    dni=int(input("Ingrese el DNI del alumno: "))
    if dni != 0:
        nombre=str(input("Ingrese el nombre: "))
        apellido=str(input("Ingrese el apellido: "))
        notas=obtener_notas()
        nombre_completo=[nombre,apellido]
        datos=[nombre_completo,notas]
        alumno=(dni,datos)
    else:
        alumno=(0,)
    return alumno

def obtener_lista_alumnos():
    lts_alumnos=[]
    alumno=obtener_alumno()
    while alumno[0] != 0:
        lts_alumnos.append(alumno)
        alumno=obtener_alumno()
    return lts_alumnos

def ordenarAluxDNI(lista_alumnos):
    alumnos = lista_alumnos.copy()
    for i in range(0, len(alumnos) - 1):
        for d in range((i+1), len(alumnos)):
            if alumnos[i][0] >= alumnos[d][0]:
                aux = alumnos[i]
                alumnos[i] = alumnos[d]
                alumnos[d] = aux
    print(alumnos)

def main():
    lista_alumnos=obtener_lista_alumnos()
    print(lista_alumnos)
    ordenarAluxDNI(lista_alumnos)
    

main()