# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Primera entrega
# ===========================================================

# GRUPO:
# INTEGRANTE 1:
#   APELLIDOS, NOMBRE:
#   DNI:
# INTEGRANTE 2:
#   APELLIDOS, NOMBRE:
#   DNI:
# INTEGRANTE 3:
#   APELLIDOS, NOMBRE:
#   DNI:



# -----------------------------------------------------------------------------
# EJERCICIO 3) EL DECODIFICADOR

# Se tiene que realizar un juego con las siguientes instrucciones:

# 1. El programa decidirá 3 dígitos no repetidos. Ej: 123
# 2. El jugador deberá indicar 3 dígitos mediante la consola.
# 3. El programa nos devolverá una pista de las siguientes:
#
#     ¡Casi!: El jugador acertó los tres números, pero en el orden incorrecto.
#     Cerca: El jugador acertó un número en la posición correcta.
#     Nada: El jugador no acertó el resto de casos.
#
# 4. Basándonos en estas pruebas, el jugador tendrá que conseguir hacer que
#    coincidan los 3 dígitos en la misma posición, el programa responderá y
#    terminará con:
#                    ¡Enhorabuena, ahora eres un hacker!

# Por ejemplo, si intentamos jugar con la máquina y esta tiene almacenado el
# número 479, esto sería un ejemplo de una partida:

# >>> juego_decodificador()
# ¡Bienvenido al decodificador!
# ¿Cuál es tú apuesta?: 459
# Cerca, ¡sigue así!
# ¿Cuál es tú apuesta? 345
# Nada, inténtalo de nuevo.
# ¿Cuál es tú apuesta? 947
# ¡Casi!, reordénalos.
# ¿Cuál es tú apuesta? 479
# ¡Enhorabuena, ahora eres un hacker!
# >>>

# Es importante que el programa termine en esa sentencia.

# Notas:
# Hay que tener en cuenta la división de las tareas para completar este tiempo
# de tareas que podrían tener una complejidad elevada. ¡Divide y vencerás!
#
# Hay algunas instrucciones que pueden ser de utilidad para desarrollar este
# sencillo juego:

import random
def juego_decodificador():
    print("¡Bienvenido al decodificador!")

    valores = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    cant_digitos = 3
    codigo = ''

    for i in range(cant_digitos):
        candidato = random.choice(valores)

        while candidato in codigo:
            candidato = random.choice(valores)
        codigo = codigo + candidato

    print("Tienes que adivinar un numero de ", cant_digitos, "cifras distintas")
    propuesta = input('¿Cuál es tú apuesta?: ')

    intentos = 3
    while propuesta != codigo and propuesta != 'error':
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0
        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos + 1
            elif propuesta[i] in codigo:
                coincidencias = coincidencias + 1
        print("Tu propuesta (", propuesta, ") tiene", aciertos, "aciertos y ", coincidencias, "coincidencias.")

        if coincidencias == 3:
            print("¡Casi!, reordénalos.")
        elif coincidencias == 2:
            print(" Cerca, ¡sigue así!")
        elif candidato == propuesta:
            print("¡Enhorabuena, ahora eres un hacker! ", intentos, "intentos realizados")
        propuesta = input("Nada, inténtalo de nuevo.  ")

    if propuesta == 'error':
        print("El codigo era", codigo)
        print("Suerte la proxima vez!")
    else:
        print("¡Enhorabuena, ahora eres un hacker! ",  intentos, "intentos realizados")
print(juego_decodificador())