import math
# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda práctica
# ===========================================================

#   APELLIDOS, NOMBRE:
#   DNI:

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

class Figura():

    def ___init___(self,perimetro,area,diametro,a,b):

        self.perimetro = perimetro
        self.area = area
        self.diametro = diametro

    def AreaCuadrado(a,b):
        area = a*b
        return area

    def PerimetroCuadrado(a,b):
        perimetro = a + a + b + b
        return perimetro

    def AreaCirculo(a):
        b = math.pi
        area = b * a ** 2
        return area

    def DiametroCirculo(a):
        diametro = a * 2
        return diametro

    def PerimetroCirculo(a):
        b = math.pi
        perimetro = 2 * b * a
        return perimetro

    def AreaTriangulo(a,b):
        area = a*b/2
        super(Figura,)
        return area

    def PerimetroTriangulo(a,b,c):
        perimetro = a+b+c
        return perimetro


class Cuadrado(Figura):
    a = 0
    b = 0

    def ___init___(self,perimetro,area):
        self.area = area
        self.perimetro = perimetro

    Figura.AreaCuadrado(a,b)
    Figura.PerimetroCuadrado(a,b)



class Circulo(Figura):
    a = 0
    def ___init___(self,perimetro,area,diametro,a,b):
        self.area = area
        self.perimetro = perimetro
        self.diametro = diametro
        self.a = a
        self.b = b


    Figura.AreaCirculo(a)
    Figura.PerimetroCirculo(a)
    Figura.DiametroCirculo(a)




class Triangulo(Figura):
    a = 0
    b = 0
    c = 0
    def ___init___(self,perimetro,area,diametro,a,b,c):

        self.perimetro = perimetro
        self.area = area
        self.diametro = diametro

    Figura.AreaTriangulo(a,b)
    Figura.PerimetroTriangulo(a,b,c)




print(" Area Cuadrado ",Cuadrado.AreaCuadrado(5,10))
print(" Perimetro Cuadrado ",Cuadrado.PerimetroCuadrado(5,5))

print(" Area Circulo ",Circulo.AreaCirculo(5))
print(" Diametro Circulo",Circulo.DiametroCirculo(5))
print(" Perimetro de un Circulo",Circulo.PerimetroCirculo(5))

print(" Area Triangulo ",Triangulo.AreaTriangulo(5,10))
print(" Perimetro Triangulo",Triangulo.PerimetroTriangulo(5,5,5))


