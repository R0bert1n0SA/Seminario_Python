import random
import sys

#Solucion del bug validacion
def Validar():
    user_answer = input("Respuesta: ").strip() 
    if user_answer.isdigit():
        num=int(user_answer)
        if num in {1, 2, 3, 4}:
            return num - 1
    print("Respuesta no válida")
    sys.exit(1) 


# Preguntas para el juego
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
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    pregunta ,opciones,respuesta=random.choice(preguntas)
    # Se muestra la pregunta y las respuestas posibles
    print(pregunta)
    for i, answer in enumerate(opciones):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        entrada=Validar()
    # Se verifica si la respuesta es correcta
        if entrada == respuesta:
            print("¡Correcto!")
            score += 1
            break
        else:
            score-=0.5
    else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(opciones[respuesta])
    # Se imprime un blanco al final de la pregunta
    print()
print("Su puntaje es: "+str(score))
