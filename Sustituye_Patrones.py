fichero = "sustituciones.txt"
frase = "1 me dijo que 0 vendría con 2"
def sustituye_patrones(frase, fichero):
    with open(fichero, "r") as f:
        fichero = f.read()
    nombres = [i for i in fichero.split()]
    nombres = "".join(nombres)
    nombres = nombres.split(":")

    nombres = [i for i in nombres if i]

    frase = frase.replace("0",nombres[0])
    frase = frase.replace("1", nombres[1])
    frase = frase.replace("2", nombres[2])
    return print(frase)

sustituye_patrones(frase,fichero)
