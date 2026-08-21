def fibonacci(n):
    a = 0
    b = 1
    c = 0 

    for contador in range (1, n + 1):        
        print(f"Termo {contador}:", b)
        c = a + b
        a = b
        b = c

fibonacci(4)


