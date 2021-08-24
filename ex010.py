print('Exercicio 10: Programa que leia quantos reais alguém tem e diz quantos doláres essa pessoa pode comprar')
r = float(input('Quantos reais você tem na carteira? R$'))
# cotação do dolar hj: R$5,38
print('Com {:.2f} você pode comprar {:.2f} doláres'.format(r, r / 5.38))
