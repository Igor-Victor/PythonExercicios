print('Exercíio 66: leitor v.2.0')
from rich import print
print('[red]=[/red]' * 30)
print('[blue]Somador[/blue]')
print('[red]=[/red]' * 30)
n = soma = quant = 0
while True:
    n = int(input('Digite um número: (999 para parar) '))
    quant += 1
    if n == 999:
        break
    soma += n
print(f'Foram mostrados {quant} números, e a soma entre eles é {soma}!')
