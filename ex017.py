import math
print('Exercício 27: programa que leia cateto oposto/adjacente de um triângulo retângulo e mostre a sua hipotenusa')
cateto_o = float(input('Insira a medida do cateto oposto:'))
cateto_a = float(input('Insira a medida do cateto adjacente:'))
hipotenusa = cateto_o ** 2 + cateto_a ** 2
print('Com base nos valores que você me mostrou, a hipotenusa desse triângulo equivale a: {:.2f}'.format(math.sqrt(hipotenusa)))
print('Agora irei mostrar esse resultado utilizando módulos. A hipotenusa é: {:.2f}'.format(math.hypot(cateto_o,  cateto_a)))



