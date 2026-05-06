# 1) Crie um programa no qual o usuário informe a idade de um número indeterminado de
# alunos. Para encerrar a leitura dos dados, o usuário deve informar uma idade negativa.
# No final, o programa deve mostrar a média aritmética entre a maior e a menor idade

idade = 0
maiorIdade = 0
menorIdade = 0

while idade >= 0:
    idade = int(input("Informe a idade: "))

    if(idade > 0 and menorIdade == 0):
        menorIdade = idade
    if(idade > 0 and idade < menorIdade):
        menorIdade = idade
    if(idade > maiorIdade):
        maiorIdade = idade

media = (menorIdade + maiorIdade) / 2
print(f"A menor é {menorIdade}")
print(f"A maior é {maiorIdade}")
print(f"A média é {media}")