def is_palindrome(word):
    formattedWord = word.lower()

    if len(word) <= 1:
        return True

    if formattedWord[0] == formattedWord[-1]:        
        is_palindrome(formattedWord[1:-1])
        return True

    return False

word = input("Informe a palavra: ")

print(is_palindrome(word))
