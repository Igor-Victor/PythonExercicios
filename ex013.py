print('\033[1;36;m-=\033[m' * 30)
print('Exercicio 13: Ajustador de salário com reajuste de 15%')
print('\033[1;36;m-=\033[m' * 30)
s = float(input('Insira o seu salário: \033[1;32;mR$\033[m'))
r = s * 15 / 100
print('Parabéns! Seu novo salário com base no reajuste de 15% é \033[1;32;mR$\033[m{:.2f}'.format(s + r))
