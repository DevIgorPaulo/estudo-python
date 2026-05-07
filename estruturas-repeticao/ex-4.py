# 4) Faça um algoritmo que leia informações de alunos (Matricula, Nota1, Nota2 , Nota3)
# com o fim das informações indicado por Matricula = 9999. Para cada aluno deve ser
# calculada a média final de acordo com a seguinte fórmula:
#  Média final = [(2 * Nota1) +(3* Nota2) +(4* Nota 3)] / 9
# Se a média final for igual ou superior a 5, o algoritmo deve mostrar Matrícula, Média
# Final e a mensagem "APROVADO".
# Se a média final for inferior a 5, o algoritmo deve mostrar Matricula, Média Final e a
# mensagem "REPROVADO".
# Ao final devem ser mostrados o total de aprovados, o total de alunos da turma e o total
# de reprovados.

totalAlunos = 0
totalAprovados = 0
totalReprovados = 0

while True:
    matricula = int(input("Informe a matricula (ou informe 9999 para sair) : "))

    if(matricula == 9999):
        break

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    mediaFinal = ((2 * nota1) +(3 * nota2) +(4 * nota3)) / 9

    if(mediaFinal >= 5):
        situacao = 'APROVADO'
        totalAprovados += 1
    else:
        situacao = 'REPROVADO'
        totalReprovados += 1

    totalAlunos += 1    

    print("===== RESULTADO =====")
    print(f"Matricula: {matricula}")
    print(f"Média: {mediaFinal}")
    print(f"Situação: {situacao}")
    print("====================")

print("==== RESULTADO GERAL ====")
print(f"Total de alunos: {totalAlunos}")
print(f"Total de alunos aprovados: {totalAprovados}")
print(f"Total de reprovados: {totalReprovados}")
print("=========================")
