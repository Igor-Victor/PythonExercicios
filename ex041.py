from datetime import date
print('Programa que determine a classe de um atleta com base em sua faixa etária')
ano = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos. '.format(idade))
if idade <= 9 :
    print('O atleta está classificado como MIRIM!')
elif 9 < idade <= 14:
    print('O atleta está classificado como INFANTIL!')
elif 14 < idade <= 19:
    print('O atleta está classificado como JUNIOR!')
elif 19 < idade <= 25:
    print('O atleta está classificado com SÊNIOR!')
elif idade > 25:
    print('O atleta está classificado como MASTER!')