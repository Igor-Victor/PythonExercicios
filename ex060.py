# fatorial com o for
"""print('Exercício 60: Fatorial com For e com While')
# fatorial com for:
n = int(input('Digite um número qualquer e eu mostrarei no seu fatorial: '))
fatorial = 1
print(f'Você escolheu o fatorial de {n}! ')
print('calculando...')
sleep(1)
print(f'{n}! = ', end=' ')
for c in range(n, -1 + 1, -1):
    print(c, end=' ')
    print('x' if c > 1 else '= ', end=' ')
    fatorial *= c
print(fatorial)"""

# fatorial com while
n = int(input('Digite um número para saber seu fatorial: '))
c = n
fatorial = 1
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '= ', end=' ')
    fatorial *= c
    c -= 1
print(fatorial)
