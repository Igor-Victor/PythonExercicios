print('Exercício 52: Programa que lê um número inteiro e diz se é ou não um número primo')
numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes!')
if total == 2:
    print('e por conta disso, ele \033[1;34mé primo\033[m')
else:
    print('e por conta disso, ele \033[1;31mnão é primo!\033[m')