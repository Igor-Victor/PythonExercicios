print('\033[1;36;m -=' * 30)
print('\033[1;33;mExercício 11: calculador de área de parede e e tinta necessária para pinta-la.\033[m')
print('\033[1;36;m -=\033[m' * 30)
print('Cada litro de tinta equivale a \033[4;33;m2m\033[m')
l = float(input('Insira aqui a largura da sua parede:'))
a = float(input('Insira aqui a altura da sua parede:'))
ar = l * a
print('A área de sua parede é de \033[4;33;m{}m²\033[m!'.format(ar))
print('Você precisa de \033[4;33;m{:.2f}\033[m litros de tinta para pinta-la por completo.'.format(ar / 2))
