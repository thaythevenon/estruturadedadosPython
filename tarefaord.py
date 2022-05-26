def bubble_sort(lista):
    ordenado = False
    while not ordenado:
        ordenado = True
        # laço
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                # faz a troca (swap)
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False
        
    return lista

def insertion_sort(lista): # tipo jogo de cartas   
    for i in range(1, len(lista)):       
        for j in range(0, i):            
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i] # troca
    
    return lista

def menor(lista, inicio=0): # retorna o indice com o menor valor
    menor = inicio # armazena indice do menor
    for i in range(inicio, len(lista)):
        if lista[i] < lista[menor]:
            menor = i
            
    return menor

def selection_sort(lista):
    for i in range(0, len(lista)):
        indice_menor = menor(lista, i)
        #indice_menor = lista.index(min(lista[i:]))
        lista[indice_menor], lista[i] = lista[i], lista[indice_menor] # troca

    return lista

  
    
## TESTES ##
lista1 = [15,13,14]
lista2 = [37, 24, 90, 13, 45]
lista3 = [5, 4, 3, 2, 1]


print("questão 1",lista1)
print(bubble_sort(lista1),insertion_sort(lista1),selection_sort(lista1))
print()

print("questão 2",lista2)
print(bubble_sort(lista2),insertion_sort(lista2),selection_sort(lista2))
print()

print("questão 3",lista3)
print(bubble_sort(lista3),insertion_sort(lista3),selection_sort(lista3))
print()
