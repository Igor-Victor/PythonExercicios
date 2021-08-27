print('Exercício 38: programa que compare dois números e diga qual é maior e qual é menor')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('Seus números são: \033[4;31;m{}\033[m e \033[4;34;m{}\033[m. '.format(n1, n2))
if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo valor é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!')
# POSSO SUBSTITUIR O ULTIMO ELIF POR ELSE
