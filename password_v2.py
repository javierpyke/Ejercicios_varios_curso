# Hacer una clase llamada Password que siga
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
# fuerte debe tener 
# 2 o mas mayúsculas
# 1 o mas minúscula
# 5 o mas digitos.

# generarPassword():  genera la contraseña del objeto con la
# longitud que tenga.

# Luego, crear un main()  ejecutable:

from random import randint


class Password:
    def __init__(self, longitud=8):
        self.longitud = longitud
        if longitud < 8:
            self.longitud = 8
        self.generarPassword()

    def generarPassword(self):
        ok = False

        while not ok:
            self.contrasenia = ""
            for i in range(self.longitud):
                # 5 o mas digitos.
                # 2 o mas mayúsculas
                # 1 o mas minúscula
                
                n = randint(1,10)
                if n <= 7:
                    self.contrasenia += str(randint(0,9))
                else:
                    if n <= 9:
                        self.contrasenia += chr(randint(ord('A'),ord('Z')))
                    else:
                        self.contrasenia += chr(randint(ord('a'),ord('z')))
            if self.esFuerte():
                ok = True

    def esFuerte(self):
        contadorMayusculas = 0
        contadorMinusculas = 0
        contadorDigitos = 0
        for letra in self.contrasenia:
            if letra.isdigit():
                contadorDigitos += 1
            elif letra.islower():
                contadorMinusculas += 1
            else:
                contadorMayusculas += 1
        return (contadorDigitos >= 5) and (contadorMayusculas >= 2) and (contadorMinusculas >= 1)

    def __str__(self):
        return "pass: " + self.contrasenia

    def __eq__(self, otroPass):
        return self.longitud == otroPass.longitud and self.contrasenia == otroPass.contrasenia


def main():
    pas = Password(8)
    print(str(pas))


main()