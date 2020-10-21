# Crea una clase NIF que se usará para mantener DNIs con su 
# correspondiente letra.
# Los atributos serán el número de DNI (entero) y la letra 
# que le corresponde.
# La clase dispondrá de los siguientes métodos:
# 
# Constructor predeterminado que inicialice el nº de DNI a
# 0 y la letra a espacio en blanco (será un NIF no válido).
# 
# Constructor que reciba el DNI y establezca la letra 
# que le corresponde.
# 
# geters y seters para el número de DNI 
# (que ajuste automáticamente la letra).
# leer(): que pida el número de DNI (ajustando 
# automáticamente la letra)
# Método que nos permita mostrar el NIF (ocho dígitos, 
# un guión y la letra en mayúscula; por ejemplo: 00395469-F)
# La letra se calculará con un método auxiliar (privado) de la
# siguiente forma:
# se obtiene el resto de la división entera del número 
# de DNI entre 23 y se usa la siguiente tabla para 
# obtener la letra que corresponde:

CLAVENIF={0:'T', 1:'R', 2:'W', 3:'A', 4:'G',5:'M',6:'Y',7:'F',8:'P',
     9:'D',10:'X',11:'B',12:'N',13:'J',14:'Z',15:'S',16:'Q',
     17:'V',18:'H', 19:'L', 20:'C', 21:'K', 22:'E'}

#OTROMASCLAVENIF = ['T','R',WAGMYFPDXBNJZSQVHLCKE"

OTROCLAVENIF = "TRWAGMYFPDXBNJZSQVHLCKE"

class NIF():
    def __init__(self,dni=0, letra=""):
        self.dni = dni
        self.letra = letra
    
    def __calcularLetra__(self):
        self.letra = CLAVENIF[self.dni%23]

    def otorgarLetra(self):
        if self.dni == 0:
            self.letra = 0
        else:
            self.__calcularLetra__()

    def __str__(self):
        return str(self.dni)+"-"+self.letra
    
def leer():
    dni=int(input("Ingrese un DNI: "))
    dni_nif = NIF(dni)
    dni_nif.otorgarLetra()
    return dni_nif


def main():
    dni1 = leer()
    print(dni1)

main()