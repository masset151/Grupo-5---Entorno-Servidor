import math


def area_cuadrado(L):
    
    area=L**2
    return  print('El area del cuadrado es: ', area)


def area_circulo(R):
    
    area=math.pi*R**2
    return print('El area del circulo es %.3f ' % area)

def area_triangulo(b,h):

    area=b*h/2
    return print('El area del triángulo es: ', area)

def area_trapecio(B,b,h):

    area=(B+b)*h/2
    return print('El area del Trapecio es: ', area)

def area_rectangulo(b,h):

    area=b*h
    return print('El area del Rectángulo es: ', area)

def area_elipse(a,b):

    area=a*b*math.pi
    return print('El area de la elipse es %.3f ' % area)