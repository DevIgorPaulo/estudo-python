quantidade_alunos = int(input("Informe a quantidade de alunos: "))
alunos = {}

for contador in range(quantidade_alunos):
    nome = input("Informe o nome do aluno: ")
    nota_1 = int(input("Primeira nota: "))
    nota_2 = int(input("Segunda nota: "))
    nota_3 = int(input("Terceira nota: "))
    nota_4 = int(input("Quarta nota: "))
    notas = [nota_1, nota_2, nota_3, nota_4]
    notas.sort()
    notas.pop(0)

    media = sum(notas) / 3
    alunos[nome] = {
        "nota_1": nota_1,
        "nota_2": nota_2,
        "nota_3": nota_3,
        "nota_4": nota_4,
        "media": media
    }

print(
    f"| {'Nome':<15} "
    f"| {'Nota 1':>7} "
    f"| {'Nota 2':>7} "
    f"| {'Nota 3':>7} "
    f"| {'Nota 4':>7} "
    f"| {'Media':>7} "
    f"| {'Situação':<10} |"
)
print("-" * 77)
for aluno, dados in alunos.items():
    situacao = "Aprovado" if dados['media'] >= 6 else "Reprovado"
    print(
        f"{aluno:<15} "
        f"{dados['nota_1']:>9.1f} "
        f"{dados['nota_2']:>9.1f} "
        f"{dados['nota_3']:>9.1f} "
        f"{dados['nota_4']:>9.1f} "
        f"{dados['media']:>10.1f} "
        f"{situacao:>12}"
    )

