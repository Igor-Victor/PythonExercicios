print('Exercício 5 - Programa que leia número inteiro e mostre na tela seu antecessor e seu sucessor.')
n = int(input('Insira um número:'))
a = n - 1
s = n + 1
print('O \033[1;35;mAntecessor\033[m de \033[31;m{}\033[m é \033[1;35m{}\033[m.'.format(n, a))
print('O \033[1;34mSucessor\033[m de \033[31;m{}\033[m é \033[1;34m{}\033[m.'.format(n, s))
