from random import randint
print('Exercício 68: Par ou ímpar')
opjog = soma = total = 0
oppc = randint(1, 10)
while True:
    opjog = int(input('Insira um número: '))
    while opjog > 10:
        opjog = int(input('Valor inválido. Digite apenas um valor entre 1 e 10.'))
    decisao = str(input('Você deseja Par ou Ímpar? [P/I] ')).strip().upper()
    soma = opjog + oppc
    if soma % 2 == 0 and decisao == 'P':
        print('~' * 50)
        print(f'Você jogou {opjog} e o Computador {oppc}. No total, deu {soma} - PAR')
        print('VITÓRIA DO JOGADOR!!')
        print('~' * 50)
        total += 1
    elif soma % 2 == 0 and decisao == 'I':
        print('~' * 50)
        print('----- GAME OVER -----')
        print(f'Você jogou {opjog} e o Computador {oppc}. No total, deu {soma} - PAR')
        print('VITÓRIA DA MÁQUINA')
        print('~' * 50)
        break
    elif soma % 2 != 0 and decisao == 'I':
        print('~' * 50)
        print(f'Você jogou {opjog} e o Computador {oppc}. No total, deu {soma} - ÍMPAR')
        print('VITÓRIA DO JOGADOR!!')
        print('~' * 50)
        total += 1
    elif soma % 2 != 0 and decisao == 'P':
        print('~' * 50)
        print('----- GAME OVER -----')
        print(f'Você jogou {opjog} e o Computador {oppc}. No total, deu {soma} - ÍMPAR')
        print('VITÓRIA DA MÁQUINA')
        print('~' * 50)
        break
print(f'Número de vitórias consecutivas: {total}')
