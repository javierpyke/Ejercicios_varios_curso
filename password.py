"""# Hacer una clase llamada Password que siga
# las siguientes condiciones:

# Atributos:   int    longitud
# String contraseña.
# Por defecto, la longitud sera de 8.

# constructores serán los siguiente:
#     Un constructor por defecto.
#     Un constructor con la longitud que nosotros le pasemos.
#     Generara una contraseña aleatoria con esa longitud.

# Los métodos que implementa serán:
# esFuerte(): devuelve un booleano si es fuerte o no, para que sea
# fuerte debe tener 2 o mas mayúsculas, 1 o mas minúscula
# 5 o mas digitos.

# generarPassword():  genera la contraseña del objeto con la
# longitud que tenga.

# Luego, crear un main()  ejecutable:"""

import random as R

caracteres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",1,2,3,4,5,6,7,8,9]
mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = [1,2,3,4,5,6,7,8,9]


class Password:
    def __init__(self,longitud=8):
        self.contrasenia=""
        self.longitud=longitud
        if longitud < 8:
            self.longitud = 8
        self.contrasenia = self.generarPassword()
    
    def generarPassword(self):
        contrasenia=[]
        for x in range(self.longitud):
            caracter = R.choice(caracteres)
            contrasenia.append(str(caracter))
        return("".join(contrasenia))

    def esFuerte(self):
        may = 0
        minus = 0
        num = 0
        for caracter in self.contrasenia:
            if caracter in mayusculas:
                may += 1
            elif caracter in minusculas:
                minus += 1
            else:
                num += 1
        if (may >= 2) and (minus >= 1) and (num >= 5):
            return True
        else:
            return False



def main():
    pass1=Password()
    print(pass1.contrasenia)
    print(pass1.esFuerte())

    
main()    

