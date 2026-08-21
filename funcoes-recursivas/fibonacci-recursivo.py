def fibonacci(n):
    if n < 3:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

termo = int(input("Informe o termo: "))
print(fibonacci(termo))