print('Exercício 44: calculador de imc')
peso = float(input('Por favor, indique o seu peso: '))
altura = float(input('Por favor, indique a sua altura: '))
imc = peso // (altura ** 2)
if imc <= 18.5:
    print('Com base em seu IMC, constatei que você está abaixo do peso ideal!')
elif imc >= 18.5 and imc <= 25:
    print('Com base em seu IMC, constatei que você está na faixa de peso ideal!')
elif imc >= 25 and imc <= 30:
    print('Com base em seu IMC, constatei que você está com sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Com base em seu IMC, constatei que você está acima da faixa de peso ideal - obesidade!!')
elif imc >= 40:
    print("Com base em seu IMC, constatei que você esta MMuito acima da faixa de peso ideal - obesidade mórbida!!")
print('Seu IMC: {}. '.format(imc))
