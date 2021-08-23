#numero1 = str(input('Digite um número: '))
#numero2 = str(input('Digite outro número: '))
#numero3 = str(input('Digite outro número: '))
#numero4 =str(input('Digite outro número: '))
#unidade = numero4
#dezena = numero3
#centena = numero2
#milhar = numero1
#número = numero1 + numero2 + numero3 + numero4
#print('Seu número é: {}. '.format(número))
#print('informações sobre seu número: ')
#print(' Unidade:{};\n Dezena:{}\n Centena:{}\n Milhar:{}. '.format(unidade, dezena, centena, milhar))

# mesma coisa porém com outro método:
numero = int(input('Diga um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Seu número é: {}! '.format(numero))
print('Unidade: {}; '.format(u))
print('Dezena: {}; '.format(d))
print('Centena: {}; '.format(c))
print('Milhar: {}. '.format(m))