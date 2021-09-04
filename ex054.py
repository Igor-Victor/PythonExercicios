print('Exercício 54: Contador de maioridade de 7 pessoas')
from datetime import date
maioridade = 0
menoridade = 0
for c in range(1, 8):
    atual = date.today().year
    nascimento = int(input(f'Por favor, digite o ano de nascimento da {c}° pessoa: '))
    idade = atual - nascimento
    if idade < 21:
        menoridade += 1
    elif idade >= 21:
        maioridade += 1
print(f'Dessas 7 pessoas, {menoridade} são menores do que 21 anos, e {maioridade} têm ou são maiores do que 21 anos!')
