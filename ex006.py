print('Exercício 6: Crie um programa que leia um número e mostre seu dobro, triplo e raíz quadrada')
n = int(input('Insira um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {};'.format(n, d))
print('O triplo de {} é {};'.format(n, t))
print('A raíz quadrada de {} é {:.2f}!'.format(n, r))