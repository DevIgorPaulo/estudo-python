numero = int(input("Informe um número entre 0 e 999: "))

if numero < 0 or numero > 999:
    print("Número inválido!")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    stringCentenas = ""
    stringDezenas = ""
    stringUnidades = ""

    if centenas > 0:
        stringCentenas = f"{centenas} centena{'s' if centenas > 1 else ''}"
    if dezenas > 0:
        stringDezenas = f"{dezenas} dezena{'s' if dezenas > 1 else ''}"
    if unidades > 0:
        stringUnidades = f"{unidades} unidade{'s' if unidades > 1 else ''}"
    
    if(stringCentenas != "" and stringDezenas != "" and stringUnidades != ""):
        print(f"{numero} = {stringCentenas}, {stringDezenas} e {stringUnidades}")
    elif (stringCentenas != "" and stringDezenas != ""):
        print(f"{numero} = {stringCentenas} e {stringDezenas}")
    elif (stringCentenas != "" and stringUnidades != ""):
        print(f"{numero} = {stringCentenas} e {stringUnidades}")
    elif (stringDezenas != "" and stringUnidades != ""):
        print(f"{numero} = {stringDezenas} e {stringUnidades}")
    elif (stringCentenas != ""):
        print(f"{numero} = {stringCentenas}")
    elif (stringDezenas != ""):
        print(f"{numero} = {stringDezenas}")
    elif (stringUnidades != ""):
        print(f"{numero} = {stringUnidades}")
