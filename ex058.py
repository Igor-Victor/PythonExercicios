print('Exercício 58: Adivinhador V.2.0')
from random import randint
from time import sleep
n = randint(0, 10)
tentativas = 0
print('Opa, vamos brincar de adivinhação então!')
numero = int(input('Pensei num número ente 1 e 10! Em que número eu pensei? '))
if numero != n:
    tentativas += 1
while numero != n:
    print('\033[32mHmm...\033[m')
    sleep(0.5)
    numero = int(input('\033[31mErrou!\033[m Não pensei nesse número. Em que número eu pensei? '))
    if numero != n:
        tentativas += 1
if numero == n:
    print(f'É isso aí!! \033[1;32mVocê acertou\033[m com \033[4m{tentativas} tentativas!!\033[m! ', end=' ')
    print(f'Eu pensei \033[32mno número {n}!\033[m')
