x, y = (int(input("Digite um numero ")), int(input("Digite outro numero ")))
opcao = 0

while opcao != 5:
    print("""O que voce deseja fazer com esses numeros?
    [1] SOMAR
    [2] MULTIPLICAR 
    [3] MAIOR 
    [4] NOVOS NUMEROS
    [5] SAIR """)
    opcao = int(input("Qual sua opção "))
    if opcao == 1:
        print('-=-'*10)
        print(f"A soma entre {x} + {y} = {x + y}")
        print("-=-"*10)
    elif opcao == 2:
        print('-=-' * 10)
        print(f"A multiplicação entre {x} x {y} = {x * y}")
        print('-=-' * 10)
    elif opcao == 3:
        print('-=-' * 10)
        print(f"O maior valor dos 2 é {max(x, y)}")
        print('-=-' * 10)
    elif opcao == 4:
        print('-=-' * 10)
        x, y = (int(input("Digite um numero ")), int(input("Digite outro numero ")))
        print('-=-' * 10)
    elif opcao == 5:
        print("Fim")
    elif opcao != 1 or 2 or 3 or 4 or 5:
        print("Opção invalida, tente novamente")



