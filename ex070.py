import os


print('Exercício 70: Lista de compras')
produto = preco = total = maisdemil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    cont += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        maisdemil += 1
    total += preco
    replay = str(input('Gostaria de cadastrar um novo produto? [S/N]')).strip().upper()[0]
    if replay == "N":
        break
print(f'Total gasto na compra: R${total:.2f}')
print(f'Foram {maisdemil} produtos com preço superior à R$1000,00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}! ')
