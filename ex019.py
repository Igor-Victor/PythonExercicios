from random import choice
print('exercício 19: Programa que sorteie entre 4 alunos.')
aluno1 = input('Insira o nome do aluno 1: ')
aluno2 = input('Insira o nome do aluno 2: ')
aluno3 = input('Insira o nome do aluno 3: ')
aluno4 = input('Insira o nome do aluno 4: ')
print('Irei sortear um destes 4.')
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi o(a): {}! '.format(choice(lista)))
