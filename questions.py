import random
import sys

#Solucion del bug validacion
def validar():
    """ Valida la entrada del usuario y la convierte en un número entre 0 y 3 """
    user_answer = input("Respuesta: ").strip() 
    if user_answer in {"1", "2", "3", "4"}:
        return int(user_answer) - 1
    print("Respuesta no válida")
    sys.exit(1) 


def evaluar(entrada,respuesta):
    """ Evalúa la respuesta del usuario y devuelve la puntuación obtenida """
    if entrada == respuesta:
        print("¡Correcto!")
        return 1
    else:
        return -0.5


def mostrar_pregunta (pregunta,opciones,respuesta,score):
    """ Muestra una pregunta al usuario y maneja la respuesta """
    print("\n" + pregunta)
    
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")  # Muestra las opciones numeradas
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        entrada = validar()
        # Se verifica si la respuesta es correcta
        valor=evaluar(entrada,respuesta)
        if valor == 1:
            score += valor
            break
    else:
        print("Incorrecto. La respuesta correcta es:")            
        print(opciones[respuesta])


def bucle(preguntas_seleccionadas,score):
    """ Itera sobre las preguntas  """
    # Se muestra la pregunta y las respuestas posibles
    for pregunta, opciones, respuesta in preguntas_seleccionadas:  
        mostrar_pregunta(pregunta,opciones,respuesta,score)
        if score < 0 :
            score=0
    return score


def principal():
    """ Ejecuta el juego de preguntas """
    preguntas=[("¿Qué función se usa para obtener la longitud de una cadena en Python?", 
            ("size()", "len()", "length()", "count()"), 1),
            ("¿Cuál de las siguientes opciones es un número entero en Python?", 
            ("3.14", "'42'", "10", "True"), 2),
            ("¿Cómo se solicita entrada del usuario en Python?", 
            ("input()", "scan()", "read()", "ask()"), 0),
            ("¿Cuál de las siguientes expresiones es un comentario válido en Python?", 
            ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario",), 3),
            ("¿Cuál es el operador de comparación para verificar si dos valores son iguales?", 
            ("=", "==", "!=", "==="), 1),]
    score=0.0
    preguntas_seleccionadas=random.sample(preguntas,3)
    print("Su puntaje es: "+str(bucle(preguntas_seleccionadas,score)))


principal()
