from math import radians, sin, cos, tan
print('Desafio 18: Programa que leia um ângulo qualquer e mostre o seno, cosseno e tangente deste ângulo')
ângulo = int(input('Insira um ãngulo qualquer:'))
print('Seu ângulo é {}°. '.format(ângulo))
print('O seno do ângulo {} é {:.2f}; '.format(ângulo, sin(radians(ângulo))))
print('O coseno dp ângulo {} é {:.2f}; '.format(ângulo, cos(radians(ângulo))))
print('A tangente do ângulo {} é {:.2f}! '.format(ângulo, tan(radians(ângulo))))


