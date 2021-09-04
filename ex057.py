print('Exercício57: Conferidor de sexo')
sexo = str(input('Informe seu sexo: [M/F]:')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[1;31mOpção inválida!\033[m Informe o seu sexo: [M/F]')).strip().upper() 
if sexo == 'M':
    sexo = '\033[34mMasculino\033[m'  # azul
if sexo == 'F':
    sexo = '\033[31mFeminino\033[m'  # rosa
print(f'Sexo registrado! Seu sexo é {sexo}.')
