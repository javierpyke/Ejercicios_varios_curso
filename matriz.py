"""Prueba Inventada de Matrices. 
Crear una listado de las ventas por vendedor de una semana 
para un local de articulos de limpieza cuyo ticket promedio 
es de 100 pesos y realiza 500 operaciones semanales.

"""

import random as R

VENDEDORES= {0:'VENDEDOR/DIA',1:'Juan',2:'Pedro',3:'Omar',4:'Ricardo',5:'Javier'}
DIAS = ["","Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]


def crearMatrix(filas, columnas,valor=0):
    m = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(valor)  # INSERTA VACIO POR PARAMETRO NO DECLARADO 
        m.append(fila)
    return m

def mostrar_listado_ventas(m):
    print("".center(100,'-')) 
    print("VENTAS SEMANALES POR VENDEDOR".center(100," "))
    print("".center(100,'-'))
    for f in range(len(m)):
        print("{:12s} ".format(VENDEDORES[f]),end = " ")
        for c in range(1,len(m[f])):            
            print("{:10s}".format(str(m[f][c])), end = " ")
        print(" ")
        
    print("".center(100,'-'))     
    print(" FIN LISTADO ".center(100,' '))
    print("".center(100,'-')) 

def generador_ventas_alea():
    vendedor = R.randint(1,5)
    dia_semana = R.randint(1,7) # el local trabaja 7 dias x semana
    venta = R.randint(1,200)#ventas ent
    return vendedor, dia_semana, venta

def main():
    #crea listado vacio
    listado_ventas_x_vendedor = crearMatrix(6,8)

    for i in range(len(DIAS)):
        listado_ventas_x_vendedor[0][i]=DIAS[i]
 
    for i in range (1): #genera 500 ventas aleatorias
        vendedor, dia, venta = generador_ventas_alea()
        listado_ventas_x_vendedor[0][dia]=DIAS[dia]
        listado_ventas_x_vendedor[vendedor][0]=VENDEDORES[vendedor]
        listado_ventas_x_vendedor[vendedor][dia] += venta
        
        
    
    mostrar_listado_ventas(listado_ventas_x_vendedor)











main()
