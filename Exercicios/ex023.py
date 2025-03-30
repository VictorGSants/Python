num = int(input(print('Digite um numero de 0 a 9999')))
n = str(num)

print("""   
 unidade{}
 dezena{}
 centena{}
 milhar{}
""".format(n[3], n[2], n[1], n[0]))