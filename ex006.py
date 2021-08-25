print('Exercício 6: Crie um programa que leia um número e mostre seu dobro, triplo e raíz quadrada.')
n = int(input('Insira um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O \033[1;35;mdobro\033[m de \033[1;36;m{}\033[m é \033[1;35;m{}\033[m;'.format(n, d))
print('O \033[1;35;mtriplo\033[m de \033[1;36;m{}\033[m é \033[1;35;m{}\033[m;'.format(n, t))
print('A \033[1;35;mraíz quadrada\033[m de \033[1;36;m{}\033[m é \033[1;35;m{:.2f}\033[m!'.format(n, r))