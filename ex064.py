print('Exercício 064: LEITOR')
contador = 0
numero = int(input('Digite um número inteiro: '))
soma = numero


while numero != 999:
    numero = int(input('Insira outro número inteiro: '))
    contador += 1
    soma += numero
print(f'Foram mostrados {contador} numeros no total!')
print(f'A soma entre todos os números, exceto "999" foi {soma - 999}.')
print('fim')
