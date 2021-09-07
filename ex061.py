print('Exercício 61: refazer exercício 51 com while')
print('-=' * 30)
print('10 primeiros termos de uma P.A - V.2.0')
print('-=' * 30)
primeirotermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razao: '))
primeiro = primeirotermo
contador = 1
while contador <= 10:
    print(f'{primeiro}', end=' → ')
    primeiro += razao
    contador += 1
print('fim!')
