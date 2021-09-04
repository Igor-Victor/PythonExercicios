print('Exercício 47: Programa que mostre todos os números pares entre 1 e 50')
print('\033[1;35;m-=\033[m' * 20)
print('\033[1;31;mNÚMEROS PARES ENTRE 1 E 50\033[m')
print('\033[1;35;m-=\033[m' * 20)
n = 50
for n in range(0, 51, 2):
    print(n, end=' ')
