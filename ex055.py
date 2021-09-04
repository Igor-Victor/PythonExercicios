print('Exercício 55: Calculador do peso de 5 pessoas, que diz o maior e o menos pesos.')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Por favor, insira o peso da {p}°  pessoa:  '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg e o menor peso é {menor}kg')

