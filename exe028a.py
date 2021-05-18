from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "PENSAR"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('En que número eu pensei? '))# Jogador tenta Adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! você conseguir me vencer! é exatamente {}'.format(jogador))
else:
    print('GANHEI! eu pensei no número {} e não no {}'.format(computador, jogador))