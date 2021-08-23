print('Exercício 12: Programa que lê preço de um produto e mostre seu novo preço com 5% de desconto')
p = float(input('Insira aqui o preço do seu produto: R$'))
d = p * 5 / 100
print('O Novo preço do seu produto é {:.2f}!'.format(p - (d)))
