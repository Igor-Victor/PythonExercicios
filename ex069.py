print('Exercício 69: Tratamento de dados')
maiordezoito = numerohomens = mulhermenor20 = idade = 0
while True:
    print('=' * 40)
    print('------- CADASTRO -------')
    print('=' * 40)
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maiordezoito += 1
    sexo = str(input('Digite o sexo: [Masculino/Feminino]')).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input('Digite o sexo: [Masculino/Feminino]')).strip().upper()[0]
    if sexo == 'M':
        numerohomens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    print('=' * 40)
    replay = str(input('Quer cadastrar uma nova pessoa? [S/N]')).strip().upper()[0]
    while replay not in "SN":
        replay = str(input('Quer cadastrar uma nova pessoa? [S/N]')).strip().upper()[0]
    if replay == "N":
        break
print('--------- ESTATÍSTICAS ---------')
print(f'Foram {maiordezoito} pessoas maiores de dezoito anos.')
print(f'Foram {numerohomens} homens cadastrados no total.')
print(f'Foram {mulhermenor20} mulheres com menos de 20 anos.')
