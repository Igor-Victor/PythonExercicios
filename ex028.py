from random import randint
print('Exercício 28: adivinhar número esolhido pelo PC.')
# fazer computador escolher número
numero = randint(1, 10)
print('Escolhi um número de 1 a 10. Que número eu escolhi?')
n = int(input('Digite um número: '))
if n != numero:
    print('Que pena! Você errou!')
    r = str(input('Quer jogar de novo? Sim ou não? ')).strip().lower()
if r == 'sim':
    print('Ok. Vamos lá então!')
    n =int(input('Digite outro número: '))
if n != numero:
    r = str(input('Que pena, você errou de novo. Quer reiniciar? ')).strip().lower()
if r == 'sim':
    print('ok, lá vamos nós de novo...')
    n = int(input('Digite outro número: '))
else:
    print('Parabéns! Vcoê acertou!!!')
