from random import randint
print('Exercício 28: adivinhar número esolhido pelo PC.')
# fazer computador escolher número
numero = randint(0, 5)
print('Escolhi um número entre 0 e 5! Que número eu escolhi?')
n = int(input('Digite um número: '))
if n != numero:
    print('Que pena! Você errou!')
else:
    print('Parabéns! Vcoê acertou!!!')
