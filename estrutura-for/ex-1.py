# 1) Escreva um programa que peça dois números inteiros e imprima todos os
# números inteiros entre eles.

inicio = int(input("Informe o número inicial: "))
fim = int(input("Informe o número final: "))
step = 1
inicio += 1

if(fim < inicio):
    step = -1
    inicio -= 2

for i in range(inicio, fim, step):
    print(i)