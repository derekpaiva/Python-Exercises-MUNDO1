#nome é a variável para o nome da pessoa
nome = input('Digite o seu nome completo: ')

#nome_corte é o nome desconsiderando os espaços em branco
nome_corte = nome.strip()

#nome_dividido é a lista com o nome seprado
nome_dividido = nome.split()

#nome_junto é a lista com os nomes juntos
nome_junto = ''.join(nome_dividido)

print('Seu nome com todas as letras maiúculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome_junto)))
print('E o seu primeiro nome possui {} letras'.format(len(nome_dividido[0])))