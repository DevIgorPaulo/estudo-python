lista = [9, 7, 2, 1, 3]
print(lista)
for i in range(1, len(lista)):
    menor = lista[i]
    j = i - 1

    while j >= 0 and menor < lista[j]:
        j -= 1