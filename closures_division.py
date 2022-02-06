def make_division_by(n):
    
    def division(x):
        assert type(n) == int and type(x) == int, "Ingresa solo numeros enteros"
        return x / n
    return division
 

    """Manera de hacerlo con lambda"""
    # division = lambda x: x / n
    #  return division

def run():
   
    division_by_3: int = make_division_by(3)
    print(division_by_3(18))

    division_by_5: int = make_division_by(5)
    print(division_by_5(100))

    division_by_18: int = make_division_by(18)
    print(division_by_18(5))

if __name__ == '__main__':
    run()

