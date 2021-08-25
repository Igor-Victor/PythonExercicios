print('\033[1;32;m-=\033[m' * 20)
print('\033[1;31;mExercício 14: Conversor de Temperaturas.\033[m')
print('\033[1;32;m-=\033[m' * 20)
Celsius = float(input('Escreva a temperatura em °C:'))
F = Celsius * 1.8 + 32
print('\033[1;32;m-\033[m' * 25)
print('{}°\033[1;31;mC\033[m é igual a {}°\033[1;36;mF\033[m!'.format(Celsius, F))
print('\033[1;32;m-\033[m' * 25)
