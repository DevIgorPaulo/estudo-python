# 9) Em uma eleição para gerência em uma empresa com 20 pessoas
# colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule
# o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
# • Cada colaborador(a) votou em uma das quatro pessoas candidatas (que
# representamos pelos números 1, 2, 3 e 4).
# • Também foram contabilizados os votos nulos (representados pelo número
# 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada
# candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a
# porcentagem de votos nulos em relação ao total de votos e a porcentagem de
# votos em branco em relação ao total de votos.

# Contadores de votos
votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0
votosCandidato4 = 0
votosNulos = 0
votosBrancos = 0

# Recebe os 20 votos
for i in range(20):
    voto = int(input(f"Informe o voto da pessoa {i+1}: "))

    if voto == 1:
        votosCandidato1 += 1
    elif voto == 2:
        votosCandidato2 += 1
    elif voto == 3:
        votosCandidato3 += 1
    elif voto == 4:
        votosCandidato4 += 1
    elif voto == 5:
        votosNulos += 1
    elif voto == 6:
        votosBrancos += 1
    else:
        print("Voto inválido!")

# Cálculo das porcentagens
porcentagemNulos = (votosNulos / 20) * 100
porcentagemBrancos = (votosBrancos / 20) * 100

# Descobrir vencedor
maiorVotos = max(
    votosCandidato1,
    votosCandidato2,
    votosCandidato3,
    votosCandidato4
)

qtdGanhadores = 0

if maiorVotos == votosCandidato1:
    ganhador = "Candidato 1"
    qtdGanhadores += 1
if maiorVotos == votosCandidato2:
    ganhador = "Candidato 2"
    qtdGanhadores += 1
if maiorVotos == votosCandidato3:
    ganhador = "Candidato 3"
    qtdGanhadores += 1
if maiorVotos == votosCandidato4:
    ganhador = "Candidato 4"
    qtdGanhadores += 1

if qtdGanhadores > 1:
    ganhador = "Houve um empate!"



# Resultado
print("\n---------------- RESULTADO ----------------")
print(f"Votos Candidato 1: {votosCandidato1}")
print(f"Votos Candidato 2: {votosCandidato2}")
print(f"Votos Candidato 3: {votosCandidato3}")
print(f"Votos Candidato 4: {votosCandidato4}")
print(f"Votos Nulos: {votosNulos}")
print(f"Votos Brancos: {votosBrancos}")
print(f"Porcentagem de Nulos: {porcentagemNulos:.2f}%")
print(f"Porcentagem de Brancos: {porcentagemBrancos:.2f}%")
print(f"Ganhador: {ganhador}")
print("-------------------------------------------")