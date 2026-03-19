#Considere que o último concurso vestibular apresentou três provas: Português, Matemática
#e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo
#o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:
#a) o nome e as notas em cada prova do candidato
#b) a média do candidato
#c) uma informação dizendo se o candidato foi aprovado ou não
#Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou
#nenhuma nota abaixo de 5.0

candidato = input("Informe o nome do candidato: ")
portugues = float(input("Informe a nota em português: "))
matematica = float(input("Informe a nota em matemática: "))
conhecimentosGerais = float(input("Informe a nota em conhecimentos gerais: "))

menorNota = min(portugues, matematica, conhecimentosGerais)
media = (portugues + matematica + conhecimentosGerais) / 3
situacao = "Aprovado" if media >= 7 and menorNota >= 5 else "Reprovado"

print("====== RESULTADO VESTIBULAR ======")
print(f"Nome do Candidato: {candidato}")
print(f"Nota em Português: {portugues}")
print(f"Nota em Matemática: {matematica}")
print(f"Nota em Conhecimentos Gerais: {conhecimentosGerais}")
print(f"Média: {media}")
print("====== RESULTADO FINAL =====")
print(f"O Aluno {candidato} foi: {situacao}")