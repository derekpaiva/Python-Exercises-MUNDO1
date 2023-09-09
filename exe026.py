frase = str(input('Digite uma frase: ')).lower().strip()

print('Analisando a frase: {}...'.format(frase.capitalize()))
print('A frase possui {} letras A'.format(frase.count('a')))
# o comando +1 após frase.find('a') acrescenta uma posição na primeira letra.
print('A primeira vez que a letra A aparece é na posição {}'.format(frase.find('a')+1))
#a função frase.rfind('a') faz com que a busca pelo carctere comece pela direita.
print('A última vez que a letra A aparece é na posição {}'.format(frase.rfind('a')))