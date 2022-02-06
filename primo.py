from typing import List


def es_primo(n: int) -> bool:
    es_primo = False
    divisores: List[int] = [x for x in range(2,n) if n % x == 0]
    resultado: bool = len(divisores) == 0

    if resultado == True:
        es_primo = True
    return es_primo
def run(n):
    print(es_primo(n))

if __name__ == '__main__':
    
    try:
      n: int = int(input("Ingrese un numero: "))

      if n > 1:
          run(n)
      else: 
          raise ValueError
    except ValueError:
        print("Ingrese un numero mayor a 1")
    
