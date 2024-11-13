import random

def ordenador_decide_jugada():
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    eleccion_usuario = input("Elige piedra, papel o tijeras:")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras:")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar():
    print("Bienvenido al juego de Piedra, Papel y Tijeras")
    jugada_ord = ordenador_decide_jugada()
    jugada_user = usuario_decide_jugada()
    resultado = determina_ganador(jugada_user, jugada_ord)
    print(f"El ordenador ha escogido {jugada_ord} y el usuario ha escogido {jugada_user}. {resultado}")
    return resultado

    
        




if __name__ == "__main__":
    jugar()