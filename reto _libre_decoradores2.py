def sombrero_seleccionador(func):
    def seleccion(random):
        func()
        casas = ["Gryffindor","Ravenclaw", "Hufflepuff", "Slyterin"]
        eleccion = casas[random]
        return print(eleccion)
    return seleccion

@sombrero_seleccionador
def random(n):
    print("Bienvenido a Hogswarts, esta es tu casa: ")

    return n 
n = random.randint(0,3)
random(n)
