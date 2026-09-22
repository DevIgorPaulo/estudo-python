produtos = {}

while True:
    codigo = int(input("Digite o código: "))

    if(codigo == 0):
        break

    if codigo in produtos:
        print("Este produto já está cadastrado! informe um novo.")
        continue
    
    quantidade = int(input("Digite a quantidade: "))
    
    produtos[codigo] = quantidade

for chave, valor in produtos.items():
    print(f"Codigo: {chave}", f"Quantidade: {valor}")
     
