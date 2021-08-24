print('Exercício 30: Programa que lê um número que o usuário digita e diz se é par ou ímpar')
numero = int(input('Digite um número por favor: '))
n = numero % 2
if n == 0:
    print('-' * 20)
    print('O número {} é par! '.format(numero))
    print('-' * 20)
else:
    print('-' * 20)
    print('O número {} é impar! '.format(numero))
    print('-' * 20)
