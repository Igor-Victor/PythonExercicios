from random import shuffle
print('Desafio 20: Programa que leia nomes de alunos e sorteie a ordem em que cada um irá apresentar.')
a1 = input('Insira o nome do aluno 1: ')
a2 = input('Insira o nome do aluno 2: ')
a3 = input('Insira o nome do aluno 3: ')
a4 = input('Insira o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
