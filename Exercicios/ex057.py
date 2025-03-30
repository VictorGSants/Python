sexo = str(input("Digite seu Sexo: [M/F] ").strip().upper())
while sexo != "M" and sexo != "F":
    sexo = str(input("Digite M ou F").strip().upper())
if sexo == "M":
    print("Sexo masculino registrado com SUCESSO")
elif sexo == "F":
    print("Sexo feminino registrado com SUCESSO")