from random import randint
from time import sleep
print('Exercício 45: Pedra, Papel, tesoura')
opções = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('\033[1;31;m=-\033[m' * 20)
print('\033[1;35;mMENU DE OPÇÕES\033[m')
print('''\033[34;m0\033[m - Pedra
\033[34m1\033[m - Papel
\033[34m2\033[m - Tesoura''')
print('\033[1;31;m=-\033[m' * 20)
jogador = int(input('Qual é a sua opção? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
if jogador == pc:
    print('Ninguém ganhou, foi empate')
if jogador == 0 and pc == 1:
    print('''OPÇÃO DO JOGADOR: Pedra
OPÇÃO DO COMPUTADOR: Papel
COMPUTADOR GANHOU!''')
if jogador == 0 and pc == 2:
    print('''OPÇÃO DO JOGADOR: Pedra
OPÇÃO DO COMPUTADOR: Tesoura
JOGADOR GANHOU!''')
if jogador == 1 and pc == 0:
    print('''OPÇÃO DO JOGADOR: Papel
OPÇÃO DO COMPUTADOR: Pedra
JOGADOR GANHOU!''')
if jogador == 1 and pc == 2:
    print('''OPÇÃO JOGADOR: Papel
OPÇÃO COMPUTADOR: Tesoura
COMPUTADOR GANHOU!''')
if jogador == 2 and pc == 0:
    print('''OPÇÃO DO JOGADOR: Tesoura
OPÇÃO DO COMPUTADOR: Pedra
COMPUTADOR GANHOU!''')
if jogador == 2 and pc == 1:
    print('''OPÇÃO DO JOGADOR: Tesoura
OPÇÃO DO COMPUTADOR: Papel
JOGADOR GANHOU!''')
