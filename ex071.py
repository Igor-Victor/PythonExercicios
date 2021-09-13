print('Exercício 71: Caixa Eletrônico')
from rich.progress import track
from time import sleep
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
cedula = 200
cedulastotais = 0
for contador in track(range(4), 'Calculando...'):
    sleep(1)

while True:
    if total >= cedula:
        total -= cedula
        cedulastotais += 1
    else:
        if cedulastotais > 0:
            print(f'Você consegue sacar {cedulastotais} de {cedula}!')
        if cedula == 200:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cedulastotais = 0
        if total == 0:
            break