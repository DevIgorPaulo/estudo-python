word = input("Informe a palavra: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'ã', 'Ã', 'õ', 'Õ', 'é', 'É', 'ô', 'Ô', 'ó', 'Ó']
totalVowels = 0

for letter in word:
    if letter in vowels:
        totalVowels += 1

print(f"Esta palavra tem: {totalVowels} vogais")