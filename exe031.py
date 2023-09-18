km = float(input('Digite a quantidade de km que sua viagem tem: '))
if km <= 200:
    p = km*0.50
else:
    p = km*0.45
print('Sua viagem custará R${:.2f}'.format(p))