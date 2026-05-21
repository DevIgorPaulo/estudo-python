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

votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0
votosCandidato4 = 0
votosNulos = 0
votosBrancos = 0

for i in range (21):
    voto = int(input("Informe o voto: "))

    if voto == 1:
        votosCandidato1 += 1
    elif voto == 2:
        votosCandidato2 +=1
    elif voto == 3:
        votosCandidato3 +=1
    elif voto == 4:
        votosCandidato4 +=1
    elif voto == 5:
        votosNulos +=1
    elif voto == 6:
        votosBrancos +=1

porcentagemNulos = votosNulos / 20 * 100 
porcentagemBrancos = votosBrancos / 20 * 100 

if (votosCandidato1 > votosCandidato2 and votosCandidato1 > votosCandidato3 and votosCandidato1 > votosCandidato4 ):
    ganhador = 1
elif (votosCandidato2 > votosCandidato1 and votosCandidato2 > votosCandidato3 and votosCandidato2 > votosCandidato4 ):
    ganhador = 2
elif (votosCandidato3 > votosCandidato1 and votosCandidato3 > votosCandidato2 and votosCandidato3 > votosCandidato4 ):
    ganhador = 3
elif (votosCandidato4 > votosCandidato1 and votosCandidato4 > votosCandidato2 and votosCandidato4 > votosCandidato3 ):
    ganhador = 4

print("-------------------- RESULTADO --------------------")
print(f"| Votos Candidatos 1:      {votosCandidato1}                      |")
print(f"| Votos Candidatos 2:      {votosCandidato2}                      |")
print(f"| Votos Candidatos 3:      {votosCandidato3}                      |")
print(f"| Votos Candidatos 4:      {votosCandidato4}                      |")
print(f"| Votos Nulos:             {votosNulos}                      |")
print(f"| Votos Brancos:           {votosBrancos}                      |")
print(f"| Porcentagem dos Nulos:   {porcentagemNulos}                   |")
print(f"| Porcentagem dos Brancos: {porcentagemBrancos}                   |")
print(f"| O GANHADOR FOI O CANDIDATO: {ganhador}                   |")
print("---------------------------------------------------")