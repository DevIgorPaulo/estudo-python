# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma
# bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas
# de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia
# com 4 elementos e a B com 10.

coloniaA = 4
coloniaB = 10

taxaA = 0.03
taxaB = 0.015

dias = 0

while coloniaA <= coloniaB:
    coloniaA += coloniaA * taxaA
    coloniaB += coloniaB * taxaB
    dias += 1

print(f"Levou {dias} para a colonia 'A' ultrapassar ou igualar a 'B'")
print("Colônia A:", round(coloniaA, 2))
print("Colônia B:", round(coloniaB, 2))