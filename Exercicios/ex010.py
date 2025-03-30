print("==== conversor de valor em dolar ====")
d = float(input(print("Insira o quanto de dinheiro em reais voçê tem")))
cotacao = 1 / 3.27

r = d * cotacao
f = round(r,3)
print("Voçê tem {} reais e {:.2f} dolares".format(d,f))
