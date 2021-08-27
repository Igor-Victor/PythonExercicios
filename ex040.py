print('Exercício 40: calculador de média v2.')
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
média = (n1 + n2) / 2
print('A média entre essas duas notas é: {:.1f}. '.format(média))
if média < 5.0:
    print('Você foi \033[1;31;mreprovado\033, sinto muito!')
elif 5.0 <= média <= 6.9:
    print('Você está de \033[1;33;mrecuperação\033[m!')
elif média > 7.0:
    print('Parabéns! Você foi \033[1;32;maprovado\033[m!')
