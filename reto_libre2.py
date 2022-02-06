import random

def sombrero_seleccionador(func):
    def seleccion():
        func()
        casas = ["Gryffindor","Ravenclaw", "Hufflepuff", "Slyterin"]
        return print(random.choice(casas))
    return seleccion

@sombrero_seleccionador
def bienvenida():
    print("Bienvenido a Hogwarts, esta es tu casa: ")

bienvenida()