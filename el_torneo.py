# DADO EL ARCHIVO "tabla_posiciones.csv" CREAR UN DICCIONARIO
# CON LOS EQUIPOS COMO CLAVE Y LOS DATOS COMO OTRO DICCIONARIO
# ANIDADO CON PJ,PG,PE,PP,GF,GC,DG

# EJEMPLO:
# d = {"Talleres":{"pj":10,"pg":10,
#                 "pe":10,"pp":10,
#                 "gf":10,"gc":10,
#                 "dg":10},{},{}}

# LUEGO GENERAR UN INDICE SOBRE EL
# DICCIONARIO CON LOS RESULTADOS DEL
# CAMPEONATO 1°,2°.... sorted....
# CALCULO PARA EL ORDENAMIENTO ES:
# puntos
# pg = 3
# pe = 1
# pp = 0

# por valores de puntos iguales

# dg

# MOSTRAR LA TABLA CON TODOS LOS DATOS

CAMINO="C:\\Users\\Alfredo\\Desktop\\Cursos ITMaster\\Python Martes Jueves Mañana\\TeleClase018\\"

class Equipo(object):
    def __init__(self,equipo,pj,pg,pe,pp,gf,gc,dg):
        self.equipo = equipo
        self.pj=pj
        self.pg=pg
        self.pe=pe
        self.pp=pp
        self.gf=gf
        self.gc=gc
        self.dg=dg
        self.pts = self.puntajes()

    def puntajes(self):
        return self.pe+self.pg*3  
        

    def __repr__(self):
        return self.equipo+self.pts

    def __str__(self):
        return "{:30s} | {:3d} | ".format(self.equipo, self.pts)

    def mostrar_campeon(self):
        print(self.equipo)

        

def cargar_tabla(nombreArchivo=""):
    lista = []
    try:
        archivo =  open(CAMINO+nombreArchivo, 'r')
    except IOError:
        print("ERROR AL ABRIR EL ARCHIVO: ",nombreArchivo)
    else:
        
        titulos = linea = archivo.readline().replace('\n','')
        linea = archivo.readline()
    
        while linea != "":
            sep = linea.replace('\n','').split(",")
            carga_equipo=Equipo(
                sep[0].replace('"',""),
                int(sep[1]),
                int(sep[2]),
                int(sep[3]),
                int(sep[4]),
                int(sep[5]),
                int(sep[6]),
                int(sep[7]))            
            lista.append(carga_equipo)
            linea = archivo.readline()
        archivo.close()
    return lista

def main():
    
    equipos=cargar_tabla("tabla_posiciones.csv")
    equipos= sorted(equipos,key=lambda x: x.pts, reverse=True  )
    print("-"*50)
    print("TABLAS DE POSICIONES")  # TITULO
    print("-"*50)
    for i in range(len(equipos)):
         print(equipos[i])
         equipos[i].puntajes()
    print("-"*50)
    print("CAMPEON", equipos[0].equipo)  # TITULO
    print("-"*50)
         
main()
