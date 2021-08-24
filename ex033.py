print('Exercício 17> Programa que lê um número e diz qual algarismo é maior e qual é menor')
valor1 = int(input('Insira o valor 1: '))
valor2 = int(input('Insira o valor 2: '))
valor3 = int(input('Insira o valor 3: '))
print('Seu valor é: {}{}{}. '.format(valor1, valor2, valor3))
# verificando quem é maior
maior = valor1
if valor2 > valor1 and valor3:
    maior = valor2
if valor3 > valor1 and valor2:
    maior = valor3
# verificando quem é menor
menor = valor1
if valor2 < valor1 and valor3:
    menor = valor2
if valor3 < valor1 and valor2:
    menor = valor3
print('O maior número é o {}, e o menor é o {}. '.format(maior, menor))
