import re
fichero = "sustituciones.txt"
frase = "1 me dijo que 0 vendría con 2"
def sustituye_patrones(frase, fichero):
    numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    with open(fichero, "r") as f:
        fichero = f.read()
    nombres = [i.rstrip("\n") for i in fichero.split(":")]

    #linea = nombres[0].split(":")
    #linea = linea.pop()
    #print(linea)
    #nombres = nombres.split(":")

    nombres = [i for i in nombres if i]



    for i in numeros:
        for x in frase:
            if x.isdigit():
                num = x.isdigit()
                frase = frase.replace(str(i),nombres[i])

    num = len(nombres)
    return frase

print(sustituye_patrones(frase,fichero))
print(sustituye_patrones("Los hijos de 4 son 3 y 5",fichero))
