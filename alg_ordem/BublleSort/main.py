from bubble import bubble_sort,selection_sort

import random

any_numbers = random.sample(range(1, 10000000000),909599)



if __name__ == "__main__":
    lista = any_numbers
    print (lista)
    
    selection_sort(lista)
    print ("ordenado:")
    print (lista)