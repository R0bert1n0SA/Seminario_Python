import random
import string
from datetime import datetime

#Ejercicio 1
def translate(text):
    """
    Aplica el descifrado ROT13 a un texto y lo divide en líneas.

    :param text: Texto de entrada a cifrar.
    :return: Lista de líneas con el texto cifrado.
    """
    rot13_table = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    )
    
    translated_text = text.translate(rot13_table)
    return translated_text.split("\n")


def filtrar_palabras(lineas):
    """
    Imprime las líneas donde la segunda palabra empieza con vocal.
    :param lineas: lista de strings.
    """
    for texto in lineas:
        t=texto.split()
        if len(t) > 1 and t[1].lower().startswith(('a', 'e', 'i', 'o', 'u')): 
            print(texto)
#------------------------------------------------------------------------------------




#Ejercicio 2
def contar(titulos):
    maximo=-99999999
    textomax=""
    for titulo in titulos:
        count=0
        for palabra in titulo:
            count+=1
        if(count > maximo):
            maximo = count
            textomax=titulo
    return textomax
#------------------------------------------------------------------------------------



#Ejercicio 3
def buscar_reglas(rules, palabra_clave):
    """
    Busca y devuelve las reglas que contienen la palabra clave.
    
    :param rules: Texto con las reglas del servidor.
    :param palabra_clave: Palabra clave ingresada por el usuario.
    :return: Lista de reglas que contienen la palabra clave.
    """
    resultado=[]
    lineas = rules.split("\n")  # Divide el texto en líneas
    for linea in lineas :
        if palabra_clave.lower() in linea.lower():
            resultado.append(linea)  
    if resultado:
        for regla in resultado:
            print(regla)
    else:
        print("No se encontraron reglas con esa palabra clave.")
#------------------------------------------------------------------------------------


#Ejercicio 4
def validar_usuario(username):
    """
    Valida si un nombre de usuario cumple con los requisitos:
    - Al menos 5 caracteres.
    - Contiene al menos un número.
    - Contiene al menos una letra mayúscula.
    - Solo puede contener letras y números.
    
    :param username: Nombre de usuario ingresado.
    """
    if len(username) < 5:
        print("\n")
        print("\n")
        print("El nombre de usuario no cumple con los requisitos.")
        return
    
    tiene_numero = False
    tiene_mayuscula = False

    for caracter in username:
        if caracter.isdigit():
            tiene_numero = True
        elif caracter.isupper():
            tiene_mayuscula = True
        elif not caracter.isalnum():  # Verifica si hay caracteres que no sean letras o números
            print("El nombre de usuario no cumple con los requisitos.")
            return

    if tiene_numero and tiene_mayuscula:
        print("El nombre de usuario es válido.")
    else:
        print("El nombre de usuario no cumple con los requisitos.")       
#------------------------------------------------------------------------------------


#Ejercicio 5
def clasificar_reaccion(tiempo_ms):
    """
    Clasifica el tiempo de reacción de un jugador en:
    - Rápido (< 200 ms)
    - Normal (200 - 500 ms)
    - Lento (> 500 ms)

    :param tiempo_ms: Tiempo de reacción en milisegundos.
    """
    if tiempo_ms < 200:
        print("Categoría: Rápido")
    elif tiempo_ms <= 500:
        print("Categoría: Normal")
    else:
        print("Categoría: Lento")
#------------------------------------------------------------------------------------

#Ejercicio 6
def contar_menciones(descriptions):
    """
    Cuenta cuántas veces aparecen las palabras clave en las descripciones.

    :param descriptions: Lista de descripciones de streams en Twitch.
    """
    conteo = {"música": 0, "charla": 0, "entretenimiento": 0}

    for descripcion in descriptions:
        palabras = descripcion.lower().split()
        for palabra in conteo:
            if palabra in palabras:
                conteo[palabra] += 1

    for palabra, cantidad in conteo.items():
        print(f"Menciones de '{palabra}': {cantidad}")
#-----------------------------------------------------------------------------------------

#Ejercicio 7
def generar_codigo(usuario) :
    """
    Genera un código de descuento único basado en el nombre de usuario y la fecha actual.

    :param usuario: Nombre del usuario para generar el código.
    :return: Un código de descuento en el formato 'USUARIO-YYYYMMDD-RANDOM'.
    """
    if len(usuario) > 15:
        print("El nombre de usuario no debe exceder los 15 caracteres.")
        return

    fecha = datetime.today().strftime("%Y%m%d")  # Formato YYYYMMDD
    aleatorio = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    codigo = f"{usuario.upper()}-{fecha}-{aleatorio}"

    print(f"Código de descuento: {codigo}")
#-----------------------------------------------------------------------------------------


#Ejercicio 8
def son_anagramas(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas.
    
    :param palabra1: Primera palabra.
    :param palabra2: Segunda palabra.
    """
    # Verificación y salida
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        print("Son anagramas.")
    else:
        print("No son anagramas.")
#-----------------------------------------------------------------------------------------

#Ejercicio 9
def limpiar_clientes(clientes):
    """
    Limpia una lista de nombres de clientes, 
    eliminando caracteres especiales y acentos, 
    y asegurando unicidad.

    :param clientes: Lista de nombres de clientes.
    :return: Lista limpia de nombres sin acentos y duplicados.
    """
    lista_limpia = []
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U'
    }
    texto_sin_acentos=""
    for cliente in clientes:
        if cliente is not None and cliente != " " and cliente != "":  
            
            for char in cliente:
                if char in acentos:
                    texto_sin_acentos += acentos[char]  # Reemplaza el carácter con acento
                else:
                    texto_sin_acentos += char  # Mantiene el carácter sin cambios
            cliente=texto_sin_acentos
            nombre_limpio = cliente.strip().title()
            if nombre_limpio not in lista_limpia:
                lista_limpia.append(nombre_limpio)
            texto_sin_acentos=""
    
    return lista_limpia
#-----------------------------------------------------------------------------------------

#Ejercicio 10

def imprimir(ronda):
    """
    Imprime el ranking de la ronda.
    :param ronda: Lista de diccionarios con las estadísticas de la ronda.
    """
    print(
        f"| {'Jugador':<10}| {'Kills':<6}| {'Asistencias':<11}| "
        f"{'Muertes':<6}| {'MVP':<6}| {'Puntos':<6}|"
        )
    print("-" * 59)
    for fila in ronda:
        print(
            f"| {fila['Nombre']:<10}| {fila['Kills']:<6}| {fila['Assists']:<11}| "
            f"{fila['Death']:<6}| {fila['MVP']:<6}| {fila['Puntos']:<6}|"
        )
        print("-" * 59)


def ordenar(ronda):
    """
    Ordena los jugadores de la ronda según sus puntos de forma descendente.
    :param ronda: Lista de diccionarios con las estadísticas de la ronda.
    """
    n = len(ronda)
    for j in range(n - 1):
        for k in range(n - j - 1):
            if ronda[k]['Puntos'] < ronda[k + 1]['Puntos']:
                ronda[k], ronda[k + 1] = ronda[k + 1], ronda[k] 




def actualizar_estadisticas(ronda,stats_ronda,total,mvp_player):
    """
    Actualiza las estadísticas de los jugadores y agrega sus datos a la lista de la ronda.

    :param ronda: Lista que contiene las estadísticas de la ronda.
    :param stats_ronda: Diccionario de estadísticas de los jugadores en la ronda actual.
    :param total: Diccionario con las estadísticas acumuladas de todos los jugadores.
    :param mvp_player: Jugador que fue el MVP de la ronda.
    """
    for player, stats in stats_ronda.items():
        total[player]['kills'] += stats['kills']
        total[player]['assists'] += stats['assists']
        total[player]['deaths'] += stats['deaths']
        total[player]['puntos'] += stats['puntos']

        # Si el jugador es el MVP, aumentar su contador
        if player == mvp_player:
            total[player]['mvp_count'] += 1  

        # Agregar a la lista de la ronda
        ronda.append({
            'Nombre': player,
            'Kills': total[player]['kills'],
            'Assists': total[player]['assists'],
            'Death': total[player]['deaths'],
            'MVP': total[player]['mvp_count'],  # Contador acumulado de MVP
            'Puntos': total[player]['puntos']
        })




def determinar_mvp(stats_ronda,round_data,mvp_player ):
    """
    Determina el jugador con más puntos (MVP) de la ronda.

    :param stats_ronda: Diccionario de estadísticas de los jugadores en la ronda.
    :param round_data: Datos de la ronda con estadísticas de cada jugador.
    :param mvp_player: Jugador MVP actual.
    :return: El jugador con más puntos.
    """
    max_puntos = -1

    for player, stats in round_data.items():
        puntos = (stats['kills'] * 3) + stats['assists']
        if stats['deaths']:
            muerte = 1
        else:
            muerte = 0
        if stats['deaths']:
            puntos -= 1
        # Guardar las estadísticas temporales para evitar recalcular
        stats_ronda[player] = {
            'kills': stats['kills'],
            'assists': stats['assists'],
            'deaths': muerte,
            'puntos': puntos
        }
        # Determinar el MVP
        if puntos > max_puntos:
            max_puntos = puntos
            mvp_player = player
    return mvp_player


def procesar_rondas(rounds, total):
    """
    Procesa todas las rondas, determina el MVP y actualiza las estadísticas.

    :param rounds: Lista de rondas con las estadísticas de los jugadores.
    :param total: Diccionario con las estadísticas acumuladas de los jugadores.
    """
    for ronda_num, round_data in enumerate(rounds, start=1):
        # Determinar si es la ronda final o numerada
        if ronda_num == 5 :
            print("Ranking ronda Final") 
        else :
            print(f"Ranking ronda {ronda_num}")
        # Lista para almacenar las estadísticas de la ronda
        ronda = []
        stats_ronda = {}
        mvp_player = None
        mvp_player=determinar_mvp(stats_ronda,round_data,mvp_player )
        actualizar_estadisticas(ronda,stats_ronda,total,mvp_player )
        ordenar(ronda)
        imprimir(ronda)











