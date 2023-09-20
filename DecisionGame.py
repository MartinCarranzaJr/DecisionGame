import random

def iniciar_juego():
    """Función principal para iniciar el juego."""
    dev = "MC project\n"
    print(dev + "-" * len(dev))
    personaje = seleccionar_personaje()
    goty = "Choose or die\n"
    print(goty + "-" * len(goty))
    introduccion(personaje)
    primer_decision()

def validar_respuesta(opciones, pregunta):
    """Solicita al usuario una respuesta y valida que esté entre las opciones permitidas."""
    while True:
        respuesta = input(pregunta)
        if respuesta in opciones:
            return respuesta
        print("No elegiste una opción válida, HAS MUERTO")
        exit()

def seleccionar_personaje():
    """Permite al usuario seleccionar un personaje y retorna la elección."""
    opciones = ["A", "B"]
    while True:
        eleccion = input("Escoge tu personaje:\nA - Hombre\nB - Mujer\n\nTu elección: ")
        if eleccion in opciones:
            return eleccion
        print("Escoge un personaje válido!")

def introduccion(personaje):
    """Introduce al usuario en la historia del juego."""
    genero = "desorientado" if personaje == "A" else "desorientada"
    print(f"Te acabas de levantar {genero} y estás en lo que parece ser un bosque,"
          " es de noche, tu mirada está borrosa y no logras ver casi nada excepto por un destello"
          " de luz que logras ver a lo lejos... empiezas a recobrar conciencia."
          " ACABAS DE RECORDAR QUE UN GRUPO DE CANÍBALES TE PERSIGUEN!")
    print("Objetivo primario: Sal con vida del bosque")

def primer_decision():
    """Solicita al usuario tomar la primera decisión del juego."""
    respuesta = validar_respuesta(
        ["A", "B"],
        "Tienes dos opciones.. puedes correr hacia un sendero que está hacia la izquierda "
        "donde se ve que hay mucho pasto o puedes ir hacia la derecha donde el camino se ve "
        "un poco más limpio.\nA - Izquierda\nB - Derecha\n\nTu elección: "
    )

    if respuesta == "A":
        camino_izquierda()
    else:
        camino_derecha()

def camino_izquierda():
    print("Has corrido hacia el sendero y te escondes en el pasto, avanzas poco a poco sin\n"
          "que te vean y haz llegado a la luz, resulta ser una casa tetrica en medio del bosque\n"
          "logras perder por poco a los canibales pero ahora no sabes que hacer.. por un lado\n"
          "hay una escotilla que parece que va hacia un sotano y por otro lado esta la puerta\n"
          "principal de la casa.")
        
    ruta1 = validar_respuesta(["A", "B"], "¿Qué quieres hacer?:\n"
                                           "A - Ir al sótano\n"
                                           "B - Entrar a la casa\n"
                                           "\n"
                                           "Elección: ")
    if ruta1 == "A":
            print("Te has encontrado con un grupo de caníbales hambrientos encerrados en el sótano, HAS MUERTO")
            exit()
    else:
        en_la_casa()

def en_la_casa():
    print("Has entrado a la casa.. A pesar de lucir tétrica por fuera, es una casa muy\n"
          "lujosa por dentro\n"
          "Hay unas llaves en la mesa de la sala de estar")

    tiene_llaves = validar_respuesta(["Si", "No"], "¿Coges las llaves?\nPodrían servir de algo, ¿no crees? \n") == "Si"
    if tiene_llaves:
        print("Cogiste las llaves\n"
              "Exploras un poco la casa hasta que escuchas que la horda de caníbales está golpeando\n"
              "la entrada, ves una puerta que parece que va hacia un garaje trasero..\n"
              "BOOOM!!!\n"
              "¡Escuchas cómo han roto la puerta los caníbales! Corres hacia el garaje\n"
              "y encuentras una motocicleta que podría servir.")
        escapar_en_moto()

    else:
        enfrenta_canibales()

def escapar_en_moto():
    validar_respuesta(["A"], "Tienes unas llaves en tu inventario\n" \
                             "A - ESCAPA EN LA MOTOCICLETA\n"
                             "\n"
                             "Selecciona: ")
    print("¡Felicidades! HAS SOBREVIVIDO y salido sano y salvo de la horda de Caníbales!")
    exit()

def enfrenta_canibales():
    print("No cogiste las llaves\n"              
          "Exploras un poco la casa hasta que escuchas que la horda de caníbales está golpeando\n"
          "la entrada, ves una puerta que parece que va hacia un garaje trasero..\n"
          "BOOOM!!!\n"
          "¡Escuchas cómo han roto la puerta los caníbales! Corres hacia el garaje\n"
          "y encuentras una motocicleta que podría servir\n"
          "No tienes llaves para encender la motocicleta\n")
    ruta1 = validar_respuesta(["A", "B"], "Parece que no tienes escapatoria.. ¿qué quieres hacer?\n"
                                          "A - Pelear con los caníbales\n"
                                          "B - Entretenerlos con algo más\n"
                                          "\n"
                                          "Respuesta: \n")
    if ruta1 == "A":
        print("Con todas tus fuerzas has luchado contra los caníbales, pero eran demasiados..\n"
              "Perdiste una mano pero ¡HAS SOBREVIVIDO!")
        exit()
    else:
        print("Intentaste entretenerlos moviendo la moto pero te alcanzaron, HAS MUERTO")
        exit()


def camino_derecha():
    item1 = False
    print("Has corrido hacia la derecha\n"
          "Corres por varios minutos hasta que te encuentras con un paso estrecho de agua en el que ves a\n"
          "un perrito atrapado en una trampa para osos\n")

    ruta1 = validar_respuesta(["A", "B"], "Escuchas aún a los caníbales que van detrás de ti\n"
                                          "¿Quieres ayudar al perrito?\n"
                                          "A - Ayudar\n"
                                          "B - Salir corriendo\n"
                                          "\n"
                                          "Decisión: ")

    if ruta1 == "A":
        item1 = True #Perrito
        aventura_con_perrito(item1)
    else:
        aventura_sin_perrito()


def aventura_con_perrito(item1):
    print("Decides ayudar al perrito. Te toma unos segundos liberarlo de la trampa, y\n"
          "él se une a ti, agradecido.\n"
          "Sigues avanzando, pero escuchas a los caníbales acercándose. Llegas a un claro\n"
          "y encuentras una vieja cabaña abandonada.")

    ruta1 = validar_respuesta(["A", "B"], "¿Qué quieres hacer?\n"
                                          "A - Esconderte en la cabaña\n"
                                          "B - Correr hacia el otro lado del claro\n"
                                          "\n"
                                          "Elección: ")

    if ruta1 == "A":
        print("Te escondes en la cabaña y el perrito te sigue. Desde una rendija puedes\n"
              "ver a los caníbales buscándote. Parece que pasaron de largo. Después de un rato,\n"
              "sales y decides que es más seguro seguir tu camino sin detenerte.")
        print("¡El perrito te ha salvado y HAS SOBREVIVIDO!")
        exit()
    else:
        print("Decides correr al otro lado del claro, pero los caníbales te han visto.\n"
              "Te persiguen, pero el perrito se sacrifica ladrando y atrayendo su atención.\n"
              "Eso te da la oportunidad de escapar.")
        print("El sacrificio del perrito te ha permitido escapar, HAS SOBREVIVIDO!")
        exit()

def aventura_sin_perrito():
    print("Decides no perder tiempo y sigues corriendo.\n"
          "Sigues avanzando y llegas a un claro con una vieja cabaña abandonada.")

    ruta1 = validar_respuesta(["A", "B"], "Tienes dos opciones:\n"
                                          "A - Esconderte en la cabaña\n"
                                          "B - Correr hacia el otro lado del claro\n"
                                          "\n"
                                          "Elección: ")

    if ruta1 == "A":
        print("Te escondes en la cabaña. Desde una rendija puedes\n"
              "ver a los caníbales buscándote. Pero sin el perrito para distraerlos,\n"
              "logran encontrar tu escondite.")
        print("Los caníbales te han encontrado, HAS MUERTO.")
        exit()
    else:
        print("Decides correr al otro lado del claro. Logras esconderte en el bosque,\n"
              "y después de un rato los caníbales desisten en su búsqueda.")
        print("A pesar de la difícil decisión, HAS SOBREVIVIDO!")
        exit()

if __name__ == "__main__":
    iniciar_juego()
