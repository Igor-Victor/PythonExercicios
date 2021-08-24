print('Exercício 26: programa que procure uma string dentro de outra string')
nome = str(input('Qual é o seu nome completo?')).strip().capitalize()
print('Seu nome tem Silva? {} '.format('SILVA' in nome.upper()))
