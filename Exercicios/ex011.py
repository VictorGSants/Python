a = float(input(print("Insira o Valor da altura: ")))
l = float(input(print("Insira o valor da largura: ")))

base = a * l

litros = base /2
f = round(litros, 2)
print("Voce tem uma parede de {}m² e vai precisar de {} litros para pintar a parede".format(base, f))

