print('Exercício 34: calculador de salário com reajuste')
salario = float(input('Me diga seu salário e calcularei o seu reajuste com base nele: R$'))
aumento10 = salario * 10 / 100
aumento15 = salario * 15 / 100
if salario > 1250:
    print('Seu novo salário com reajuste de 10% é: R${:.2f}. '.format(salario + aumento10))
else:
    print('Seu novo salário com reajuste de 15% é: R${:.2f}. '.format(salario + aumento15))
