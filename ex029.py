print('Exercício 29: Programa que leia a velocidade de um carro.')
print('Limite de velocidae: 80KM/H ---- multa: R$7,00 por quilômetro fora do limite!!!')
km = int(input('Qual é a velocidade do seu carro? '))
multa = (km - 80) * 7
if km > 80:
    print('Você ultrapassou o limite de velocidade por {}KM/H! '.format(km - 80))
    print('Você pagará de multa por sua infração: R${}! '.format(multa))
else:
    print('Você está dentro do limite de velocidade. Parabéns!')