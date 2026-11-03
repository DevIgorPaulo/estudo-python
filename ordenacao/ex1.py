lista = [9, 7, 2, 1, 3]
print(lista)
for i in range(0, len(lista) - 1):
    menor = i
    for c in range(i+1, len(lista)):
        if lista[c] <= lista[menor]:
            menor = c

    lista[i], lista[menor] = lista[menor], lista[i]

print(lista)