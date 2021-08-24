from random import randint
print('Exercício 28: adivinhar número esolhido pelo PC.')
# fazer computador escolher número
numero = randint(1, 10)
print('Escolhi um número de 1 a 10. Que número eu escolhi?')
n = int(input('Digite um número: '))
if n != numero:
    print('Que pena! Você errou!')
else:
    print('Parabéns! Vcoê acertou!!!')
