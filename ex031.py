print('Exercício 31: Programa que pergunte a distância de uma viagem em quilômetros.')
# TABELA
print('=' * 60)
print('TABELA DE PREÇOS:')
print(' R$0.50 por quilômetro para viagens de até 200km\n R$0.45 por quilômetro para viagens mais longas')
print('=' * 60)
# VARIÁVEIS
km = int(input('Digite a distância da sua viagem(em quilômetros) por favor: '))
passagem1 = 0.50 * km
passagem2 = 0.45 * km
# CONDIÇÃO
print('Distância que você colocou: {:.1f}km. '.format(km))
if km <= 200:
    print('A sua passagem para esta viagem é: R$:{:.2f}. '.format(passagem1))
else:
    print('A sua passagem para esta viagem é: R${:.2f}. '.format(passagem2))
print('Obrigado por usar os nossos serviços!')
