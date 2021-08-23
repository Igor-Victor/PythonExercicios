print('exercício 11: calculador de área de parede e e tinta necessária para pinta-la')
print('Cada litro de tinta equivale a 2m')
l = float(input('Insira aqui a largura da sua parede:'))
a = float(input('Insira aqui a altura da sua parede:'))
ar = l * a
print('A área de sua parede é de {}m²!'.format(ar))
print('Você precisa de {:.2f} litros de tinta para pinta-la por completo.'.format(ar / 2))
