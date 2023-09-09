nome = str(input('Digite o seu nome completo: ')).strip().title()

nome_list = nome.split()

print('Seu primeiro nome é {}'.format(nome_list[0]))

# o comando nome_list[len(nome_list)] pede para mostrar a posição em relação a quantidade de palavras na lista.

# mas, essa quantidade é sempre um valor a mais do que a posição, por isso o -1.

print('Seu último nome é {}'.format(nome_list[len(nome_list)-1]))