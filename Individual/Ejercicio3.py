# -----------
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
#El += hace que t se sume con la multiplicacion de i sea pues "t=t+i"
            t += i * i
    return t

print(suma_cuadrados([9,4,2,6,8,1]))


# b) Dada una lista de números l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_fórmula([2,4,6,8,10])
# 110

def suma_formula(l):
    num = len(l)
    t = 0
    l1 = [(i+1)*l[i] for i in range(num)]
    for k in l1:
        t+=k
    return t


print(suma_formula([2,4,6,8,10]))


# c) Dados dos listas numéricas de la misma longitud, representado dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos.

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def sqrt(n):
    return n**(1/2.0)

def distancia(l0,l1):
    n  = len(l0)
    l2 = [(l0[i]-l1[i])**2 for i in range(n)]
    t = 0
    for i in range(n):
        t+=l2[i]
    return sqrt(t)

print(distancia([3,1,2],[1,2,1]))


# d) Dada una lista y una funcion de un argumento, devolver la lista de los
#    resultados de aplicar la funcion a cada elelmento de la lista.

# Ejemplo:

# >>> map_mio(abs,[-2,-3,-4,-1])
# [2, 3, 4, 1]

def map_mio(f,l):
    l1 = [ f(a) for a in l]
    return l1

print(map_mio(abs,[-2,-3,-4,-1]))

# e) Dada un par de listas (de la misma longitud) y una funcion de dos
#    argumentos, devolver la lista de los resultados de aplicar la funcion a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.

# Ejemplo:
# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio(f,l0,l1):
    l2 = [f(l0[i],l1[i]) for i in range(len(l0))]
    return l2

print(map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9]))


# f) Dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero.

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(l):
    num = len(l)
    l1 = [ 1 for i in range(num) if (l[i] % 3 == 0 and l[i] != 0)]
    return sum(l1)

print(m3_no_nulos([4,0,6,7,0,9,18]))


# f) Dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3

def cuenta_coincidentes(l0,l1):
    num = len(l0)
    t = sum([ 1 for i in range(num) if l0[i] == l1[i] ])
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

def dic_posiciones_coincidentes(l0,l1):
    num = len(l0)
    l2 = {i:l0[i] for i in range(num) if l0[i]==l1[i]}
    return l2

print(dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6]))
print(dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6]))
