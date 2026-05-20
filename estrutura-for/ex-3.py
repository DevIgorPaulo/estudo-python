# 3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de
# um serviço da empresa, precisamos verificar se as notas são válidas. Então,
# escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar
# se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita
# até que a pessoa usuária insira um valor válido.

# for i in range(1, 16):
#     valido = False

#     while valido == False:
#         nota = int(input(f"Informe a {i}° nota: "))
#         if(0 <= nota <= 5):
#             valido = True

c = 1

while c <= 15:
    nota = int(input(f"Informe a {c}ª nota: "))
    if(0 <= nota <= 5):
        c += 1
    else:
        print("Nota inválida, repita!")