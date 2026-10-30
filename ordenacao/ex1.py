lista = [10, 7, 8, 6, 2, 1, 5, 7, 8, 4, 11, 10]
# lista_ordenada = []
# tamanho = len(lista)

# while tamanho > 0:
#     for i in lista:
#         menor = True
#         for c in lista:
#             if(i > c):
#                 menor = False

#         if(menor):
#             tamanho -= 1
#             lista_ordenada.append(i)
#             lista.remove(i)
        

# print(lista_ordenada)


# for indice, valor in enumerate(lista):
#     for indice2, valor2 in  enumerate(lista):
#         if(valor < valor2):
#             lista[indice], lista[indice2] =  lista[indice2], lista[indice]

for key, value in enumerate(lista):
    minKey = key

    for i in range(key + 1, len(lista)):
        if lista[i] <= lista[minKey]:
            minKey = i

    lista[key], lista[minKey] = lista[minKey], lista[key]
    

print(lista)
        

