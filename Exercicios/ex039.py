import datetime

anoNasc = int(input('Digite o ano que voce nasceu: '))
ano = datetime.date.today().year
idade = ano - anoNasc
falta = 18 - idade
passou = idade - 18
if idade > 18:
    print(f'Voce tem {idade} anos em {ano}')
    print(f'Voce ja passou {passou} ano(s) da idade de se alistar ')
    print(f'Seu aloistamento foi em {ano - passou}')
elif idade < 18:
    print(f'Voce ainda vai se alistar, faltam {falta} ano(s)')
    print(f'Seu alistamento sera em {ano + falta}')
else:
    print('Esta na hora de se alistar. SE ALISTE AGORA !')
