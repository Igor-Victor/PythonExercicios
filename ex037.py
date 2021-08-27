print('Exercício 37: Conversor de bases')
num = int(input('Digite um número inteiro: '))
print('Seu número é: {}! '.format(num))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O valor {} convertido para BINÁRIO é: {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O valor {} convertido para OCTAL é: {}. '.format(num, oct(num)[2:]))
elif opção == 3:
    print('O valor {} convertido para HEXADECIMAL é: {}. '.format(num, hex(num)[2:]))
else:
    print('Desculpe, não entendi. Tente novamente, por favor!')
