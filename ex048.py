print('Exercício 48: Soma dos números ímpares múltiplos de 3 entre 1 e 500')
n = 500
s = 0
for n in range(0, 501, 3):
    if n % 2 != 0:
        s += n
print('A soma dos multiplos ímpares de 3 entre 1 e 500 é: {}. '.format(s))
