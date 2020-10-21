"""Crear una función atributoTriple que recibe por parámetro una lista de números
	enteros y retorne un mensaje ( Texto ) de acuerdo a las características de la lista que
	figuran en la tabla 1 (más abajo).
	
	Tabla 1 - Mensajes según característica de una lista:
	
	MENSAJE		Descripción del atributo de la lista
	”Un Triple” 	Si la lista contiene solamente un conjunto de exactamente tres
			valores iguales consecutivos .
	”Dos Triples” 	Si la lista contiene exactamente dos conjuntos de exactamente
			tres valores iguales consecutivos .
	“+ Triples” : 	Si la lista contiene exactamente tres o más conjuntos de
			exactamente tres valores iguales consecutivos .
	“NADA” : 	Si la lista no cumple con ninguna de las tres especificaciones
			anteriores.
	Desde el programa principal, invocar a la función cargarListaAleat (desarrollada en
	ejercicio anterior), crear una lista con can cantidades valores generados en forma
	aleatoria entre un intervalo a y b , inclusive. Los valores can, a y b deberán ser
	previamente ingresados por el usuario. Luego, una vez cargada la lista, se deberá pasar
	por parámetro la lista cargada a la función atributoTriple y se deberá imprimir el
	mensaje que retorna.
	
	Aclaración: Se recomienda realizar pruebas directas (en intérprete en modo interactivo)
	con la función atributoTriple para verificar su correcto funcionamiento. A
	continuación algunos ejemplos de pruebas directas:
		atributoTriple ([1,2,2,2,4,4,1])             ==> Un Triple
		atributoTriple ([1,2,2,2,4,4,1,3,3,3])       ==> Dos Triple
		atributoTriple ([1,2,2,2,4,4,1,3,3,3,5,5,5]) ==> + Triple
		atributoTriple ([1,2,2,1,2,])                ==> NADA"""

import random as R

def obtener_numero():
    numero=int(input("Ingrese un numero entero positivo: "))
    while numero < 0:
        numero=int(input("Ingrese un numero entero positivo: "))
    return numero

def cargarListaAleat(indiceA,indiceB,cantidad):
    lista=[]
    for x in range(cantidad):
        numero=R.randint(indiceA,indiceB)
        lista.append(numero)
    return lista

def atributoTriple(lista):
    triples=0
    i=2
    for i in range(len(lista)):
        if lista[i] == lista[i-1] == lista[i-2]:
            triples+=1
    if triples == 0:
        return "NADA"
    elif triples == 1:
        return "Un triple"
    elif triples == 2:
        return "Dos triples"
    else:
        return "+ triples"
    

def main():
    indiceA=obtener_numero()
    indiceB=obtener_numero()
    cantidad=obtener_numero()
    if indiceA <= indiceB:
        lista=cargarListaAleat(indiceA,indiceB,cantidad)
    else:
        lista=cargarListaAleat(indiceB,indiceA,cantidad)
    resultado=atributoTriple(lista)
    print(lista)
    print(resultado)


main()
