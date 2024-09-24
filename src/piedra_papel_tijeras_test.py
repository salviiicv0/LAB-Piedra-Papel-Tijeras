from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    '''
    Test para la función ordenador_decide_jugada.
    '''
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print("El ordenador eligió:", eleccion)
    print()

# Función principal
if __name__ == "__main__":
    test_ordenador_decide_jugada()