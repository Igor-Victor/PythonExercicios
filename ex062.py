from rich import print
print('[bold blue]Exercício 62: P.A turbinado!![/bold blue]')
primeirotermo = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
primeiro = primeirotermo
contador = 1
total = 0
repeat = 10
while repeat != 0:
    total += repeat
    while contador <= total:
        print(primeiro, end=' → ')
        primeiro += razao
        contador += 1
    print('pausa')
    repeat = int(input('Deseja ver mais quantos termos? '))
print(f'Fim, com {total} termos mostrados.')