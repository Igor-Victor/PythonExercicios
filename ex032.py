from datetime import date
print('Exercício 32: Programa que leia um ano qualquer e diga se é bissexto ou não. ')
ano = int(input('Me diga um ano qualquer, se quiser saber sobre esse ano, digite "0": '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto. '.format(ano))
else:
    print('O ano {} não é bissexto. '.format(ano))
