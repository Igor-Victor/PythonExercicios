import random
print('Exercício 45: pedra papel e tesoura')
print('Vamos brincar de pedra, papel e tesoura?')
armas = ['pedra', 'papel', 'tesoura' ]
arma = str(input('Qual arma você escolhe? Pedra, papel ou tesoura?')).strip().lower()
if arma == 'pedra':
    print(random.choice(armas))