cidade = str(input(print('Digite o nome de sua cidade')))
p = cidade.strip().title().find('Santo')

if p == 0:
    print('Sua cidade começa com Santo')

else:
    print('Sua cidade nao começa com santo')

