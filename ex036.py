print('Exercício 36: Programa que aprove ou não o financiamento de uma casa.')
valor = float(input('qual é o valor da casa? \033[1;32;mR$\033[m'))
salario = float(input('Qual é o seu salário atual? \033[1;32;mR$\033[m'))
anos = int(input('Em quantos anos você quer pagar? '))
prestação = valor // (anos * 12)
if prestação > salario * 30 / 100:
    print('Você infelizmente não poderá financiar esta casa em {} anos, pois o valor da prestação excede 30% do seu salário!'.format(anos))
    print('Escolha outra prestação, ou uma casa mais barata por favor!')
else:
    print('Você pode financiar esta casa em {} anos. '.format(anos))
print('Valor da prestação: \033[1;32;mR${}\033[m'.format(prestação))
