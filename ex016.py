import math
print('Exercício 16: Programa que leia um número Real e mostre a sua porção inteira')
numero_real = float(input('Insira qualquer número real, e eu exibirei a sua porção inteira: '))
print('=' * 25)
print('A porção inteira de {:.3f} é {}!'.format(numero_real, math.floor(numero_real)))
print('=' * 25)
