print('Exercício 3: Programa que veja 2 números e mostre a soma entre eles.')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre \033[32;m{}\033[m e \033[31;m{}\033[m vale \033[4;30;m{}\033[m'.format(n1, n2, s))
