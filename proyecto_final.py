from random import choice
from datetime import datetime
from time import strftime
import pytz

def sombrero_seleccionador(func):
    def seleccion(n_alumnos: int):
        func(n_alumnos)
        cont = 1
        alumnos = {}
        while cont <= n_alumnos:
            try:
                nom_alumno = str(input("Ingresa tu nombre: ")).lower()
                if nom_alumno.isalpha() == False:
                    cont = 1
                    raise ValueError
            except ValueError:
                print("Por favor ingresa un nombre valido, procura solo ingresar letras")
            else:
                casas = ["Gryffindor","Ravenclaw", "Hufflepuff", "Slyterin"]
                eleccion = choice(casas)
                alumnos[nom_alumno] = eleccion
                london_timezone = pytz.timezone("Europe/London")
                london_date = datetime.now(london_timezone)
                print("Tu casa es:",eleccion)
                print("Tu eleccion se dio el dia:", london_date.strftime(("%d/%m/%Y, %H:%M:%S")),"Hora Londres")
            cont += 1
        print("Lista de estudiantes asignados:")
        my_list = list(alumnos.items())
        generator = (student for student in my_list)
        for element in generator:
            print(element)
    return seleccion



@sombrero_seleccionador
def alumnos(n_alumnos) -> int:
    print("Bienvenido a Hogwarts, una vez escribas el nombre, te dira la casa a la que perteneces")

    return n_alumnos


def run() -> int:

    validation = True
    while validation == True:
        try:
            n_alumnos=int(input("Cuantos alumnos desea evaluar?: "))
            if n_alumnos < 1:
                raise ValueError
            elif n_alumnos is str:
                raise ValueError
        except ValueError:
            print("Ingresa un numero valido")
            validation = True
        else:
            
            alumnos(n_alumnos)
            break


if __name__ == '__main__':
    run()

# my_dicts = {

#     "Harry:Gryffindor",
#     "Draco:Gryffindor"
# }

# generator = (student for student in my_dicts)
# for element in generator:
#     print(element)