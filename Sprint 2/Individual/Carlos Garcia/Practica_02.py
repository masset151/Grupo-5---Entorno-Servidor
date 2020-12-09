# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda práctica
# ===========================================================

#   APELLIDOS, NOMBRE: García Acevedo, Carlos
#   DNI: 77869085D

# Práctica 2: Programación orientada a objetos
# =================================

# En esta práctica veremos algunos ejercicios de Python, con una
# orientación a objetos.

# -----------
# EJERCICIO 1
# -----------
#
# Escribir una clase general llamada "Figura" con los atributos de
# cualquier figura geométrica. Posteriormente se pide implementar las
# clases "Círculo", "Cuadrado" y "Triángulo" con sus correspondientes
# atributos y funciones.

# En este ejercicio os tendréis que enfrentar con la herencia entre clases,
# colocando toda la información general en la clase "Figura" y 
# posteriormente sobreescribir esos métodos con los diferentes
# comportamientos de cada figura.

# Por ejemplo:
#
# La clase "Cuadrado" tendrá una función area donde se devolverá el 
# area de un cuadrado.
#
# Nota: Son necesarios los siguientes datos, perímetro, area, diámetro.
import math

def myCirculo():
    try:
        print("-- Eligio circulo --")
        r = float(input("Escribe el valor del radio: "))
        a = (math.pi*pow(r, 2))
        myFormat = "El area del circulo es: {}"
        print("La area es: {} u^2" .format(a))
    except:
            print ("\n--> solo puedes escribir numeros, ahora volvera al menu principal. <--\n")
def myTriangulo():
    try:
        print("-- Eligio triangulo --")
        b = float(input("Escribe el valor de la base: "))
        h = float(input("Escribe el valor de la altura: "))
        a = (b * h) / 2
        myFormat = "El area del triangulo es: {}"
        print(myFormat.format(a))
    except:
        print("\n--> solo puedes escribir numeros, ahora volvera al menu principal. <--\n")

def myCuadrado():
    try:
        print("-- Eligio cuadrado --")
        l = float(input("Escribe el valor del lado: "))
        a = l ** 2
        myFormat = "El area del cuadrado es: {}"
        print(myFormat.format(a))
    except:
        print("\n--> solo pudes escribir numeros, ahora volvera al menu principal. <--\n")

        print("-- Programa para calcular el area --")
        options = 0
        while options != 4:
            try:
                options = int(input("-- menu --\n1.circulo 2.triangulo 3.cuadrado 4.salir\n--> "))
                if(options == 1):
                    myCirculo()
                if(options == 2):
                    myTriangulo()
                if(options == 3):
                    myCuadrado()

            except:
                print("\n--> elige una opcion valida. <--\n")
