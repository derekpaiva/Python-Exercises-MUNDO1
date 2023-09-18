import random
n1 = int(input('Adivinhe que número de 0 a 5 eu escolhi: '))
c = random.randrange(0,6)
if n1 == c:
    print('Você acertou! parabéns!')
else:
    print('Poxa, você perdeu! Eu escolhi o número {}'.format(c))