from time import sleep
print('-=-' * 20)
produto = float(input('Qual é o preço do seu produto ? '))
x = int(input(print("""Qual a forma de pagamento ? 
Digite:
1 - À vista dinheiro/cheque (DESCONTO DE 10%)
2 - À vista no cartão (DESCONTO DE 5%)
3 - Em até 2x no cartão (PREÇO PADRÃO)
4 - Em 3x ou mais (20% DE JUROS)""")))
din = (produto/100) * 10
card = (produto/100) * 5
juros = (produto/100) * 20
print('-=-' * 20) 
print('CALCULANDO............')
sleep(2)
if x == 1:
    print(f'Seu desconto foi de R$: {din} valor a ser pago sera de R$: {produto - din} reais.')
elif x == 2:
    print(f'Seu desconto foi de R$: {card} valor a ser pago sera de R$: {produto - card} reais.')
elif x == 3:
    print(f'Seu desconto foi de R$: 0,00 valor a ser pago sera de R$: {produto} reais.')
elif x == 4:
    print(f'Seu juros foi de R$: {juros} valor a ser pago sera de R$: {produto + din} reais.')
else:
    print('Este numero não existe, tente novamente !')