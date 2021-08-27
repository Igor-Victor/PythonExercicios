import datetime
print('Programa que determine a classe de um atleta com base em sua faixa etária')
n1 = int(input('Digite o dia de seu nascimento: '))
n2 = int(input('Digite o mês do seu nascimento: '))
n3 = int(input('Digite o ano do seu nascimento: '))
nascimento = datetime.date(day = n1, month = n2, year = n3)