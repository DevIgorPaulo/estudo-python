lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))

if(lado1 < 0 or lado2 < 0 or lado3 < 0):
    print("Informe valores válidos!")
    exit()

if((lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1):
    if(lado1 == lado2 and lado2 == lado3):
        print("Este triângulo é Equilatero!")
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("Este triângulo é Isósceles!")
    else:
        print("Este triângulo é Escaleno!")
else:
    print("Não é triângulo!")