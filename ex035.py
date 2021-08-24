print('Exercício 35: programa que diz se 3 retas podem formar um triângloV1.0')
reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Você pode formar um triângulo com essas retas.')
else:
    print('Você não pode formar um triângulo com essas retas.')
