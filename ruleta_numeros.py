"""Desarrollar un función ruleta que solicite al usuario el ingreso de un número entero
	positivo. Ese número representará la cantidad de números al azar que deberán ser
	cargados en una lista. Generar los valores aleatorios entre el valor 0 y el valor 36
	(inclusive). La función deberá retornar la lista cargada con números aleatorios.
	Desarrollar un función porcentual que recibe por parámetro la lista generada en la
	función ruleta . La función porcentual deberá imprimir en pantalla la cantidad de
	veces que salió (aparece en lista) cada valor y el porcentaje que representa (con
	respecto al total de la muestra). No mostrar aquellos números que no hayan salido.
	Desde el programa principal invocar a ruleta e imprimir la lista que retorna la función.
	Luego invocar a porcentual pasándole por parámetro la lista generada en ruleta .
	Ejemplo de salida generado por porcentual :
		El número 8 salió 1 vez (10%).
		El número 14 salió 2 veces (20%).
		El número 20 salió 4 veces (40%).
		El número 23 salió 1 veces (10%).
		El número 30 salió 2 veces (20%)."""

import random as R

def estaEnLista(numero,lista):
    return numero in lista

def obtener_numero():
    numero=int(input("Ingrese un numero entero positivo: "))
    while numero < 0:
        numero=int(input("Ingrese un numero entero positivo: "))
    return numero

def inserOrd(lista,numero):
    i=0
    limite=len(lista)
    while i <= limite:
        if i == limite:
            lista.append(numero)
        elif numero < lista[i]:
            auxiliar=lista[i]
            lista[i]=numero
            numero=auxiliar
        i+=1

def cargarListaOrdenada(limiteA,limiteB,cantidad):
    lista=[]
    for x in range(cantidad):
        numero = R.randint(limiteA,limiteB)
        if len(lista) == 0:
            lista.append(numero)
        else:
            inserOrd(lista,numero)
        
    return lista

def sacar_porcentaje(numeros):
    repeticiones=1
    for i in range(len(numeros)):
        if i == 0:
            actual=numeros[i]
        elif numeros[i] == actual:
            repeticiones+=1
        else:
            promedio=round(repeticiones*100/len(numeros),2)
            print("El número",actual,"salió",repeticiones,"veces (",promedio,").")
            actual=numeros[i]
            repeticiones=1
        

def main():
    cantidad=obtener_numero()
    numeros=cargarListaOrdenada(0,36,cantidad)
    print("Lista generada:",numeros)
    sacar_porcentaje(numeros)

main()