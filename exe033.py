n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = n1
menor = n1

if n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3

if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3

print('O número {} é o maior'.format(maior))
print('O número {} é o menor'.format(menor))