#O sistema de avaliação de determinada disciplina, é composto por três provas. A primeira
#prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Faça um algoritmo para calcular
#a média final de um aluno desta disciplina
prova1 = float(input("Informe a nota da primeira prova: "))
prova2 = float(input("Informe a nota da segunda prova: "))
prova3 = float(input("Informe a nota da terceira prova: "))

media = ((prova1 * 2) + (prova2 * 3) + (prova3 * 5)) / (2 + 3 + 5)
print(f"Sua média foi: {media}")