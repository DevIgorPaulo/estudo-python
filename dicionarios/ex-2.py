alunos = {}

while True:
    matricula = int(input("Digite o número da matrícula: "))

    if matricula == 0:
        break

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    alunos[matricula] = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

for matricula, aluno in alunos.items():
    print(f"Matricula: {matricula}", f"Nome: {aluno["nome"]}", f"Idade: {aluno["idade"]}", f"Curso: {aluno["curso"]}")