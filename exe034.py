s = float(input('Digite o valor de seu salário: '))
if s <= 1250:
    sq = s*1.15
    print('Seu salário terá um aumento de 15%, que resultará em R${:.2f}'.format(sq))
else:
    sd = s*1.10
    print('Seu salário terá um aumento de 10%, que resultará em R${:.2f}'.format(sd))