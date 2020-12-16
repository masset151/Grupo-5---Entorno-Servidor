# -*- coding: utf-8 -*-
# practica-01.py
# Inteligencia Artificial, tercer curso del Grado de Ingeniería Informática -
# Tecnologías Informáticas. Universidad de Sevilla.

import math

# Práctica 1: Introducción a Python
# =================================

# En esta práctica veremos algunos ejercicios de Python, para ir
# familiarizándonos con el lenguaje.


# EJERCICIO 1
# -----------
#
# Escribir una función cuadrados(l) que recibiendo una secuencia l de números,
# devuelve la lista de los cuadrados de esos números, en el mismo orden.


# Por ejemplo:
#
# >>> cuadrados([4,1,5.2,3,8])
# [16, 1, 27.040000000000003, 9, 64]

# Hacer dos versiones: una usando un bucle explícito, y la otra mediante
# definición de listas por comprensión.
# Por comprensión:

def cuadrados1(l):
    a = [ a*a for a in l ]
    return a
print(cuadrados1([1,2,3,4,5]))

# Usando bucle:

def cuadrados2(l):
    a = []
    for i in l:
        a.append(i*i)
    return
print(cuadrados1([1,2,3,4,5.5]))



# -----------
# EJERCICIO 2
# -----------
# Definir una funcion vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayúsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------

def vocales_consonantes(s):
    vocales = "AEIOUaeiou"
    for i in s:
        if vocales.find(i)==-1:
            print('{0} es consonante'.format(i))
        else:
            print('{0} es vocal'.format(i))
print(vocales_consonantes("sevilla"))


# EJERCICIO 3
# -----------

# Usando como técnica principal la definición de secuancias por comprensión,
# definir las siguientes funciones:

# a) Dada una lista de números naturales, la suma de los cuadrados de los
#    números pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120
def suma_cuadrados(l):
    t = 0
    for i in l:
        if i % 2 == 0:
            t += i * i
    return t


print(suma_cuadrados([2, 4, 5, 6]))


# b) Dada una lista de números l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_fórmula([2,4,6,8,10])
# 110


def suma_formula(l):
    n = len(l)
    t = 0
    l1 = [(i + 1) * l[i] for i in range(n)]
    for k in l1:
        t += k
    return t


print(suma_formula([2, 1, 3]))


# c) Dados dos listas numéricas de la misma longitud, representado dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos.

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178
def sqrt(n):  # Devuelve la raíz cuadrada del número pasado en el parámetro
    return n ** (1 / 2.0)


def distancia(l1, l2):
    n = len(l1)
    l3 = [(l1[i] - l2[i]) ** 2 for i in range(n)]
    t = 0
    for i in range(n):
        t += l3[i]
    return sqrt(t)


print(distancia([3, 1, 2], [1, 2, 1]))


# d) Dada una lista y una funcion de un argumento, devolver la lista de los
#    resultados de aplicar la funcion a cada elelmento de la lista.

# Ejemplo:

# >>> map_mio(abs,[-2,-3,-4,-1])
# [2, 3, 4, 1]
def map_mio(f, l):
    l1 = [f(a) for a in l]
    return l1
print(map_mio(abs,[-2,-3,-4,-1]))

# e) Dada un par de listas (de la misma longitud) y una funcion de dos
#    argumentos, devolver la lista de los resultados de aplicar la funcion a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.


# Ejemplo:
# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio(f, l1, l2):
    l3 = [f(l1[i], l2[i]) for i in range(len(l1))]
    return l3
print(map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9]))



# f) Dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero.

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(l):
    n = len(l)
    l1 = [1 for i in range(n) if (l[i] % 3 == 0 and l[i] != 0)]
    return sum(l1)
print(m3_no_nulos([4,0,6,7,0,9,18]))

# f) Dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3

def cuenta_coincidentes(l1, l2):
    n = len(l1)
    t = sum([1 for i in range(n) if l1[i] == l2[i]])
    return t
print(cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6]))

# g) Dadas dos listas de la misma longitud, devolver un diccionario que tiene
# como claves las posiciones  en las que coinciden los elementos de ambas
# listas, y como valor de esas claves, el elemento coincidente.

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(l1, l2) -> object:
    n = len(l1)
    l3 = {i: l1[i] for i in range(n) if l1[i] == l2[i]}
    return l3
print(dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6]))
print(dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6]))
# -----------
# EJERCICIO 4
# -----------
# Un número es perfecto si es la suma de todos sus divisores (excepto él
# mismo). Definir una función filtra_perfectos(n,m,p) que imprime por pantalla
# todos los números perfectos entre n y m que cumplen la condición p. Se pide
# también que se indiquen los divisores de cada número perfecto que se
# imprima.

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------

def divisores(x):
    return [i for i in range(1, x) if x % i == 0]

def filtra_perfectos(a,b,f):
    for x in range(a, b+1):
        if (x == sum(divisores(x)) and f(x)):
            print("El " , x , " es perfecto y sus divisores son " , divisores(x))

# EJERCICIO 5
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros
# entre 0 y 50.
# Definir una función histograma_horizontal(d), que recibiendo un diccionario
# de ese tipo, escribe un histograma de barras horizontales asociado,
# como se ilustra en el siguiente ejemplo:

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves
# ---------------------------------------------------------------------------
d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}


def histograma_horizontal(d1):
    for x,y in sorted(d1.items()):
        if(y>=0 and y<=50):# Si esta en el rango se imprime los puntos
            print( x , ": ", y * '*')
        else:
            print('Te has pasado de rango')
print(histograma_horizontal(d1))


# -----------
# EJERCICIO 6
# -----------
# Con la misma entrada que el ejercicio anterior, definir una funcion
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical.

# Ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *
#           *
#           *
#           *
#           *
#         * * *
#         * * *
#         * * *
#       * * * *
#       * * * *
#       * * * *
#     * * * * * *
#     * * * * * *
#   * * * * * * * *
#   * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# a b c d e f g h i j

# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves
# ---------------------------------------------------------------------------

d2 = {"a": 5, "b": 7, "c": 9, "d": 12, "e": 15, "f": 20, "g": 15, "h": 9, "i": 7, "j": 2}


# Buscamos el máximo de todos para saber por cual empezar.
def histograma_vertical(d2):
    max_num = max(d2.values())  # Sacamos el valor maximo
    items = sorted(d2.items())  # ordenamos lo items
    for x in range(max_num + 1):  # Ponemos el mas uno por que el contador empieza desde cero
        print(*(
            '*'  # Si el numero maximo es menos se imprime el *
            if max_num - x < v
            else  # Si es mayor se va imprimiendo espacios
            ' '
            for k, v in items  # k es la key y v es el valor de la key
        ))
    print(*d2.keys())  # Solo mostramos las keys


print(histograma_vertical(d2))
