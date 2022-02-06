
def es_palindromo(func):
    def validador(palabra):
        func(palabra)
        palabra = palabra.replace(" ", "").lower()
        validacion = palabra == palabra[::-1]

        if validacion == True:
           return print("La palabra es palindroma")
        else:
            return print("La palabra no es palindroma")
    return validador

@es_palindromo
def palabra(palabra):
    return print("La palabra es: ", palabra)
palabra("Reconocer")