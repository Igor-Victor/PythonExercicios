from random import randint
from time import sleep
print('Exercício 28: adivinhar número esolhido pelo PC.')
# fazer computador escolher número
numero = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('Ok! Pensei em um número entre 0 e 5!')
print('Que número eu escolhi?')
n = int(input('Digite um número: '))
if n != numero:
    print('Que pena! Você errou! Eu pensei no número {}!'.format(numero))
else:
    print('Parabéns! Você acertou!!!')
