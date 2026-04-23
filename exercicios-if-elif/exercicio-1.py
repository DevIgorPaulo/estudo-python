produto1 = float(input("Informe o preço do primeiro produto: "))
produto2 = float(input("Informe o preço do segundo produto: "))
produto3 = float(input("Informe o preço do terceiro produto: "))

if(produto1 < produto2 and produto1 < produto3):
    print("Compre o primeiro produto!")
elif(produto2 < produto2 and produto2 < produto3):
    print("Compre o segundo produto!")
elif(produto3 < produto1 and produto3 < produto2):
    print("Compre o terceiro produto!")