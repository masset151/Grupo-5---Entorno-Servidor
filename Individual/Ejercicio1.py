import math

#Ejercicio 1
#def cuadrados(l)
#    return [x*x for x in l]

#Usando bucle
def cuadrados1(l):
    x = []
    for i in l:
        x.append(i*i)
    return x

print(cuadrados1([4,1,5.2,3,8]))

#Por compresión
def cuadrados2(l):
    x=[x*x for x in l]
    return x

print(cuadrados2([4,1,5.2,3,8]))
