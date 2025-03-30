from random import randint

print("-=-" * 10)
print("VAMOS JOGAR IMPAR OU PAR")
print("-=-" * 10)
while True:
    pc = randint(1, 10)
    num = int(input("Diga um valor "))
    pi = str(input("Voce quer par ou impar? [P/N] ? ").strip().upper())
    if pi == "P" and (num + pc) % 2 == 0:
        print("-"*30)
        print(f"Voce venceu ! Vc jogou {num} e o computador {pc}. total deu {num + pc} par")
        print("Vamos jogar novamente...")
        print("-=-" * 10)
        if (num + pc) % 2 != 0:
            break
    if pi == "I" and (num + pc) % 2 != 0:
        print("-" * 30)
        print(pc)
        print(f"Voce venceu ! Vc jogou {num} e o computador {pc}. total deu {num + pc} impar")
        print("Vamos jogar novamente...")
        print("-=-" * 10)
    else:
        # (num + pc) % 2 == 0:
        break

print(f"Voce perdeu ! o computador escolheu {pc} ")
