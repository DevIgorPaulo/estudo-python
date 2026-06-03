# 4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada


lista = []

for i in range (5):
    lista.append(int(input(f"Informe o {i + 1}º valor: ")))

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])