word = input("Informe a palavra: ")
wordLength = len(word) - 1
counter = 0
isPalindrome = True

while counter <= wordLength:
    if (word[counter].lower() != word[wordLength - counter].lower()):
        isPalindrome = False
        break
    counter += 1
    

if isPalindrome:
    print(f"{word} é um palindromo")
else:
    print(f"{word} não é um palindromo")
