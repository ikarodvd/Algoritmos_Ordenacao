from selectionSort import selection_Sort

import random

any_numbers = random.sample(range(1, 1000),90)



if __name__ == "__main__":
    lista = any_numbers
    print (lista)
    
    selection_Sort(lista)
    print ("ordenado:")
    print (lista)