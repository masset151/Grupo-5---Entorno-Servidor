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
    espacio = " "
    for i in s:
        if vocales.find(i)==-1:
            if espacio.find(i)==-1:
                print('{0} es consonante'.format(i))
            else:
                print('ESPACIO'.format(i))
        else:
            print('{0} es vocal'.format(i))

print(vocales_consonantes('Dragon Ball'))
