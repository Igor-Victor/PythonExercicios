print('Exercício 56: Analisador')
media = 0
maisvelho = 0
nomevelho = ''
mulheresmenos20 = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip().upper()
    media += idade
    if pessoa == 1 and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
print(f'A média de idade do grupo é {media // 4}.')
print(f'O homem mais velho do grupo é o {nomevelho}, com {maisvelho} anos.')
print(f'Temos {mulheresmenos20} mulheres com menos de 20 anos.')

