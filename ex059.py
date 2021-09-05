print('Exercício 59: Menu de opções')
valor1 = float(input('Por favor, insira um valor: '))
valor2 = float(input('Por favor, insira outro valor: '))
soma = valor1 + valor2
multiplicar = valor1 * valor2
maior = ''

print(f'\033[32;4m{"MENU":^30}\033[m')
print('por favor, escolha uma opção:')
print('''\033[1;34m[ 1 ]\033[m - SOMAR
\033[1;34m[ 2 ]\033[m - MULTIPLICAR
\033[1;34m[ 3 ]\033[m - MAIOR
\033[1;34m[ 4 ]\033[m - NOVOS NÚMEROS
\033[1;34m[ 5 ]\033[m - SAIR''')
opcao = int(input('Qual é a sua opção? '))

while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
    opcao = int(input('Valor inválido! Tente novamente: '))
if valor1 > valor2:
    maior = valor1
else:
    maior = valor2
if opcao == 1:
    print('Você escolheu a função \033[4mSOMA\033[m')
    print(f'A soma dos valores \033[1;32m{valor1:.1f}\033[m e \033[1;31m{valor2:.1f}\033[m é: \033[4m{soma:.1f}!\033[m')
elif opcao == 2:
    print('Você escolheu a função \033[4mMULTIPLICAÇÃO\033[m')
    print(f'O produto da multiplicação entre \033[1;32m{valor1:.1f}\033[m e \033[1;31m{valor2:.1f}\033[m é: ', end='')
    print(f'\033[4m{multiplicar:.1f}\033[m')
elif opcao == 3:
    print('Você escolheu a função \033[4mMAIOR\033[m')
    if valor1 == valor2:
        print('Os dois números são iguais. Não há maior, nem menor.')
    else:
        print(f'Entre \033[1;32m{valor1:.1f}\033[m e \033[1;31m{valor2:.1f}\033[m, o maior é \033[4m{maior}.\033[m')
elif opcao == 4:
    print('Você escolheu a função \033[4mNOVOS VALORES\033[m')
    valor1 = float(input('Insira o novo valor 1: '))
    valor2 = float(input('Insira o novo valor 2: '))
else:
    print('Você escolheu \033[1;33mSAIR\033[m')
    print('\033[1;32mSaindo...\033[m')
    exit()
