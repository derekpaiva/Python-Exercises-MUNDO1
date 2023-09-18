from random import randint
from time import sleep

print('-==-' *20)
print('Eu vou pensar em um número de 0 a 5, você consegue adivinhar?')
num = randint(0,5)
print('-==-' *20)
adv = int(input('Em que número eu pensei?: '))

print('PROCESSANDO...')
sleep(3) #função de tempo para que o programa faça um delay em segundos

if adv == num:
    print('Você ganhou! Eu pensei nmesmo no número {}!'.format(num))
else:
    print('Eu ganhei! Eu não pensei no {} e sim no {}!!!'.format(adv, num))