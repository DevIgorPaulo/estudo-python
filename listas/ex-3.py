# 3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista.
# Exemplo: [1,4,7,2,4].

lista = []

for i in range (5):
    lista.append(int(input(f"Informe o {i + 1}º valor: ")))

print(lista)