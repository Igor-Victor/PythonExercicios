print('Exercício 4: Programa que lê algo do teclado e dê todas as informações possíveis sobre')
a1 = input('Digite alguma coisa:')
print('O tipo primitivo de {} é: '.format(a1))
print(type(a1))
print('"{}" é alfanumerico? '.format(a1), a1.isalnum())
print('"{}" é alfabeto? '.format(a1), a1.isalpha())
print('"{}" é decimal? '.format(a1), a1.isdecimal())
print('"{}" é um dígito? '.format(a1), a1.isdigit())
print('"{}" é identifier? '.format(a1), a1.isidentifier())
print('"{}" está somente em minúsculo? '.format(a1), a1.islower())
print('"{}" está somente em maiúsculo? '.format(a1), a1.isupper())
print('"{}" é um número? '.format(a1), a1.isnumeric())
print('"{}" é imprimível? '.format(a1), a1.isprintable())
print('"{}" é um espaço? '.format(a1), a1.isspace())
print('"{}" está capitalizado?? '.format(a1), a1.istitle())

