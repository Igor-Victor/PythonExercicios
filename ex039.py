from datetime import date
print('Exercício 39: programa que diga com base na data de nascimento de alguém se ele deve se alistar ou nao')
atual = date.today().year
ano = int(input('Ano de seu nascimento: '))
print('Ano do seu nascimento: {}. '.format(ano))
idade = atual - ano
print('Quem nasceu em {}, tem {} anos em {}. '.format(ano, idade, atual))
if idade == 18:
    print('Você deve ir se alistar \033[4;31;mIMEDIATAMENTE!!\033[m')
elif idade < 18:
    print('Você ainda não precisa se alistar! Só daqui a \033[4;31;m{} anos\033[m.'.format(18 - idade))
elif idade > 18:
    print('Você já deveria ter se alistado a \033[4;31;m{} anos!\033[m '.format(idade - 18))
