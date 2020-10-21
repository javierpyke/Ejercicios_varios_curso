"""Una consultora cuenta con información de sus bases de datos, 
	que son los siguientes tres archivos (que no tienen ningún 
	criterio de ordenamiento):
	Archivo Estructura de datos Ejemplo de contenido
	provincias.txt (archivo CSV)
		ID_provincia (entero)
		nombre(cadena de caracteres)
		ID_pais
			1,Buenos Aires,1
			8,Jujuy,1
			3,Rio Grande,2
			9,San Diego,2
	localidades.txt (archivo CSV)
		ID_localidad (entero)
		nombre (cadena de caracteres)
		ID_provincia (entero)
		superficie (entero)
		poblacion (entero)
			1,Adolfo Alsina,1,14222,12
			12,San Salvador,8,1234,32
			81,La Paz,9,887,999
			53,Lujan,1,1234,10
			71,Ezeiza,1,220,101
	paises.txt (archivo CSV)
		ID_pais (entero)
		nombre (cadena de caracteres)
		ID_idioma (entero)
			1, Argentina, 1
			2, Brasil, 5
	
	8.1. Realizar la función poblacion(ID_provincia) que
	reciba como parámetro el ID de la provincia e imprime por
	consola la cantidad habitantes para dicha provincia,
	indicando además el nombre de la provincia.
	
	Ejemplo de salida : Para poblacion(1), la salida debería ser -
		Buenos Aires: 123 Habitantes
	
	8.2. Realizar una función localidadMaxima() que imprime por
	consola la localidad con mayor cantidad de habitantes indicando, 
	cantidad de habitantes, nombre de la localidad, nombre de la
	provincia y nombre del país.
	
	Ejemplo de salida:
		Población: 999
		Localidad: La Paz
		Provincia: San Diego
		Pais: Brasil"""


"""
PAISES = [ID{},ID{},ID{}]
PAIS(ID) = {"nombre":str,"idioma":int,"provincias":[{},{},{}]}
PROVINCIA(ID) = {"nombre":str,"pais"={}}
LOCALIDAD(ID) = {"nombre":str,"provincia"={},"superficie"=int,"poblacion"=int}
"""

def leerDatos(linea):
    datos=linea.split(",")
    return int(datos[0]),datos[1],int(datos[2])

def leerPaises(archivo):
    paises = {}
    archivo_paises = open(archivo,"r")
    linea_pais = archivo_paises.readline().replace("\n","")
    while linea_pais != "":
        id_pais,nombre_pais,idioma_pais = leerDatos(linea_pais)
        paises[id_pais] = {"nombre":nombre_pais,"idioma":idioma_pais,"provincias":{}}
        linea_pais = archivo_paises.readline().replace("\n","")
    return paises

def agregarProvincias(archivo,diccionario_paises):
    archivo_provincias = open(archivo,"r")
    linea_provincia = archivo_provincias.readline().replace("\n","")
    while linea_provincia != "":
        id_provincia,nombre_provincia,id_pais = leerDatos(linea_provincia)
        diccionario_paises[id_pais]["provincias"][id_provincia] = {"id_pais":id_pais,"nombre":nombre_provincia,"localidades":{}}
        linea_provincia = archivo_provincias.readline().replace("\n","")

def datosLocalidades(linea):
    datos = linea.split(",")
    return int(datos[0]),datos[1],int(datos[2]),int(datos[3]),int(datos[4])

def agregarLocalidades(archivo,diccionario_paises):
    archivo_localidades = open(archivo,"r")
    linea_localidades = archivo_localidades.readline().replace("\n","")
    while linea_localidades != "":
        id_localidad,nombre_localidad,id_provincia,superficie,poblacion = datosLocalidades(linea_localidades)
        id_provincia_pais = diccionario_paises[id_provincia]


def main():
    diccionario_paises = leerPaises("paises.csv")
    diccionario_provincias = leerProvincias("provincias.csv")
    diccionario_localidades = leerLocalidades("localidaes.csv")

main()