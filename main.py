import random

preguntas = {
    'Quien ganó el trofeo mvp en la final de la Champions league de 2015?': 'Andrés Iniesta',
    'Que equipo ganó la Champions League en el año 1998?': 'AC Milan',
    'Cuántos balones de oro ganó Ronaldo Nazário?': '2',
    'Cual es el nombre de Kroos?': 'Toni',
    'En que año el Barcelona ganó su última champions?': '2015',
    'Quien es el máximo goleador del Real Madrid?': 'Cristiano Ronaldo',
    'Que equipo ganó la Champions League en el año 2005?': 'Liverpool',
    'Que equipo ganó la Champions League en el año 1987': 'Oporto',
    'Que selección ganó el mundial en el año 2010?': 'España',
    'Quien ganó el balón de oro en el año 2019?': 'Leo Messi',
    'Que selección ganó el mundial en el año 2022?': 'Argentina'}

vidas = 3
pista_disponible = True

preguntas_list = list(preguntas.items())
random.shuffle(preguntas_list)

for pregunta, respuesta in preguntas_list:
    print(f"Te quedan {vidas} vidas.")
    print(pregunta)
    if pista_disponible:
        pista = input("¿Quieres una pista? (Sí/No) ").lower()
        if pista == "sí":
            pista_disponible = False
            if respuesta == 'Andrés Iniesta':
                print("Es un jugador español.")
            elif respuesta == 'AC Milan':
                print("Es un equipo italiano.")
            elif respuesta == '2':
                print("Ganó ambos premios en 1997 y 2002.")
            elif respuesta == 'Toni':
                print("Es un jugador alemán.")
            elif respuesta == '2015':
                print("Fue la temporada 2014-2015.")
            elif respuesta == 'Cristiano Ronaldo':
                print("Es un jugador portugués.")
            elif respuesta == 'Liverpool':
                print("Es un equipo inglés.")
            elif respuesta == 'Oporto':
                print("Es un equipo portugués.")
            elif respuesta == 'España':
                print("El torneo se celebró en Sudáfrica.")
            elif respuesta == 'Leo Messi':
                print("Es un jugador argentino.")
            elif respuesta == 'Argentina':
                print("El torneo se celebró en Qatar.")
    respuesta_usuario = input("Tu respuesta: ")
    if respuesta_usuario == respuesta:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta era {respuesta}.")
        vidas -= 1
        if vidas == 0:
            print("¡El juego ha terminado!")
            break
