#Eliminar repetidos de una lista con for:

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

# def run():
#     random_list = [1,1,2,2,4]
#     print(remove_duplicates(random_list))

# if __name__ == '__main__':
#     run()

#Eliminando elementos repetidos de una lista con sets:
def remove_duplicates(some_list):
    return print(list(set(some_list)))
def run():
    list = [1,1,2,2,4]
    remove_duplicates(list)

if __name__ == '__main__':
    run()