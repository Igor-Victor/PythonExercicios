from rich import print
print('Exercício 63: Programa que lê o primeiros n números de Fibonacci com base nesse n')
print('[bold red]-=[/bold red]' * 20)
print('[yellow] FIBONACCI [/yellow]')
print('[bold red]-=[/bold red]' * 20)
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('[red]=[/red]' * 70)
print(f'{t1} → {t2} ', end= '')
t3 = t1 + t2
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(f'→ {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('→ [italic blue]fim.[/italic blue]')
print('[red]=[/red]' * 70)
