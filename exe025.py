nome = str(input('Qual é o seu nome completo? ')).strip()
nome2 = nome.title()

print('O seu nome é {} \n E ele possui Silva? {}'.format(nome2, 'Silva' in nome2))