from random import randint

GENERALA = {1: ["UNO            ", 1],
            2: ["DOS            ", 2],
            3: ["TRES           ", 3],
            4: ["CUATRO         ", 4],
            2: ["CINCO          ", 5],
            6: ["SEIS           ", 6],
            7: ["ESCALERA       ", 25],
            8: ["FULL           ", 35],
            9: ["POKER          ", 45],
            10: ["GENERALA       ", 55],
            11: ["GENERALA DOBLE ", 1000]}

#PAPELITO = [][]
#CREAR MATRIZ [JUEGADAS][JUGADORES] EN CERO
#PONER EL VALOR (PUNTOS) EN CADA CUADRO
#AL FINAL ANTES DE MOSTRAR AL GANADOR MOSTRAR LA MATRIZ


def verDado(unDado):
    return "["+str(unDado)+"]"


def getDado():
    return randint(1, 6)


def getCubilete():
    cub = []
    for d in range(5):
        cub.append(getDado())
    return cub


def verCubilete(unCubilete):
    for d in range(5):
        print(verDado(unCubilete[d]), end=" ")


def llenarConJugadores():
    return {1:["Juan",0],2:["Pedro",0],3:["Rosa",0]}


# cubilete[1,2,2,2,2] ==> frecuencia [0, 1, 4, 0, 0, 0, 0]
#         0                             c1 c2 c3 c4 c5 c6
# 1,2,3,4,5 ==> [0,1,1,1,1,1,0]
# 2,3,4,5,6 ==> [0,0,1,1,1,1,1]
# 1,3,4,5,6 ==> [0,1,0,1,1,1,1]
# cinco unos

def esEscalera(frecuencia):
    return frecuencia.count(1) == 5 and (frecuencia[6] == 0 or
                                         frecuencia[1] == 0 or
                                         frecuencia[2] == 0)


def esGenerala(frecuencia):
    return 5 in frecuencia


def esPoker(frecuencia):
    return 4 in frecuencia


def esFull(frecuencia):
    return 2 in frecuencia and 3 in frecuencia


def getFrecuencia(cubilete):
    frec = [0, 0, 0, 0, 0, 0, 0]

    for dado in cubilete:
        frec[dado] += 1

    return frec


def verJugada(frecuencia, tiro):
    puntos = 0

    if tiro == 7 and esEscalera(frecuencia):
        puntos = GENERALA[tiro][1]
    elif tiro == 8 and esFull(frecuencia):
        puntos = GENERALA[tiro][1]
    elif tiro == 9 and esPoker(frecuencia):
        puntos = GENERALA[tiro][1]
    elif tiro == 10 and esGenerala(frecuencia):
        puntos = GENERALA[tiro][1]
    elif tiro == 11 and esGenerala(frecuencia):
        puntos = GENERALA[tiro][1]

    return puntos
#{1:["Juan",0],2:["Pedro",0],3:["Rosa",0]}

def mostrarGanador(jugadores):
    maximo = -1
    
    for k in jugadores.keys():
         if jugadores[k][1] > maximo:
             maximo = jugadores[k][1]
             nombre = jugadores[k][0]
    
    print("GANADOR: ",nombre)


def main():
    jugadores = llenarConJugadores()

    for tiro in GENERALA.keys():
        print("\nJUGANDO AL: ", GENERALA[tiro][0])
        for jugador in jugadores:
            cubilete = getCubilete()
            frecuencia = getFrecuencia(cubilete)
            
            if tiro <= 6:
                puntos = frecuencia[tiro]*tiro
            
            else:
                puntos = verJugada(frecuencia, tiro)

            print("\njuega: ", jugadores[jugador][0], end="   ")
            verCubilete(cubilete)
            jugadores[jugador][1] +=  puntos
            print(" ==> ",puntos,"  ACUMULADO: ",jugadores[jugador][1])
            
        print("")
        mostrarGanador(jugadores)

main()