print('Exercício 4: Programa que lê algo do teclado e dê todas as informações possíveis sobre.')
a1 = input('Digite alguma coisa:')
print('O tipo primitivo de {} é: '.format(a1))
print(type(a1))
print('"{}{}" é alfanumerico? '.format('\033[31;m', a1), '\033[;m', a1.isalnum())
print('"{}{}" é alfabeto? '.format('\033[31;m', a1), '\033[m', a1.isalpha())
print('"{}{}" é decimal? '.format('\033[31;m', a1), '\033[m', a1.isdecimal())
print('"{}{}" é um dígito? '.format('\033[31;m', a1),'\033[m', a1.isdigit())
print('"{}{}" é identifier? '.format('\033[31;m', a1),'\033[m', a1.isidentifier())
print('"{}{}" está somente em minúsculo? '.format('\033[31;m', a1), '\033[m', a1.islower())
print('"{}{}" está somente em maiúsculo? '.format('\033[31;m', a1), '\033[m', a1.isupper())
print('"{}{}" é um número? '.format('\033[31;m', a1), '\033[m', a1.isnumeric())
print('"{}{}" é imprimível? '.format('\033[31;m', a1), '\033[m', a1.isprintable())
print('"{}{}" é um espaço? '.format('\033[31;m', a1), '\033[m', a1.isspace())
print('"{}{}" está capitalizado?? '.format('\033[31;m', a1), '\033[m', a1.istitle())

