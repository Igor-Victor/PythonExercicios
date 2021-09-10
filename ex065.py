print('Exercício 65: Leitor e calculador de médias/maior e menor')
resposta = 'S'
media = soma = termos = maior = menor =  0
while resposta in "Ss":
    numero = int(input('Digite um valor: '))
    termos += 1
    soma += numero
    if numero == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N]')).strip()
media = soma / termos
print(f'Você digitou {termos} números, e a média entre eles foi {media}!')
