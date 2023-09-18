from datetime import date

ano = int(input("Digite um ano qualquer com os 4 dígitos! Coloque 0 caso queira o ano atual:  "))

if ano == 0: # condição para o ano atual
    ano = date.today().year # comando para considerar o ano (year) da máquina

# "and" significa "e" (o mesmo que na Matemática), assim como "or" significa "ou"
# o operador != significa "diferente"
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))