from time import sleep
print('Exercício 49: Refazer a tabuada porém desta vez com a estrutura de repetição for')
print('\033[1;m-=\033[m' * 20)
print('\033[1;34;mTabuada\033[m \033[1;31;mV2.0\033[m')
print('\033[1;m-=\033[m' * 20)
p = 1
n = int(input('Digite um número de 1 a 10, por favor: '))
print('\033[1;32;mCalculando...\033[m')
sleep(2)
if 0 <= n <= 10:  # simplificando n >= 0 and n <= 10
    print('\033[1;31;m=\033[m' * 15)
    for p in range(1, 11):
        print('{} x {} = \033[1;32;m{}\033[m'.format(n, p, n * p))
    print('\033[1;31;m=\033[m' * 15)
else:
    print('Valor \033[1;31;mINVÁLIDO!\033[m')

