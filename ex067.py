print('Exercício 67: Tabuada com loop while True')
from rich import print
print('[pink]~[/pink]' * 20)
print('[red]Tabuada V3.0[/red]')
print('[pink]~[/pink]' * 20)
n = 0
while True:
    cont = 0
    n = int(input('De qual número deseja ver a tabuada? '))
    print('[red]=[/red]' * 30)
    if n < 0:
        break
    while cont < 10:
        cont += 1
        multi = n * cont
        print(f'{n} x {cont} = {multi}')
    print('[red]=[red]' * 30)
    