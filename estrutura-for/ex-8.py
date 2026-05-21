# 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de
# previdência. Escreva um programa que leia as idades de uma quantidade não
# informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-
# 75] e [76-100]. Encerre a entrada de dados com um número negativo.

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
idade = 0

while idade >= 0:
    idade = int(input("Informe a idade: "))

    if(0 <= idade <= 25):
        intervalo1 += 1
    elif( 26 <= idade <= 50):
        intervalo2 += 1
    elif(51 <= idade <= 75):
        intervalo3 += 1
    elif(76 <= idade <= 100):
        intervalo4 += 1

print(f"Há {intervalo1} pessoa(s) entre 0 e 25 anos")
print(f"Há {intervalo2} pessoa(s) entre 26 e 50 anos")
print(f"Há {intervalo3} pessoa(s) entre 51 e 75 anos")
print(f"Há {intervalo4} pessoa(s) entre 76 e 100 anos")

