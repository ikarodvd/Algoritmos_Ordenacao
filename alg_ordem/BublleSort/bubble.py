def bubble_sort(lista):
    n = len(lista)
    for i in range (n-1): #compara elementos no bubble sort
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1] = lista[i+1], lista[i] #permutando elementos  

def selection_sort (lista):
    n = len(lista)
    for j in range (n-1): #troca elementos até tudo estar ordenado
        min_index = j
        for i in range (j,n):
            if lista[i]<lista[min_index]:
                min_index = i
        if lista [j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
            