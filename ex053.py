print('Exercício 53: Programa que diz se uma frase é ou não um palíndromo')
frase = str(input('Diga uma frase: ')).strip().lower().replace(' ', '')
invertido = frase[:: -1]
if frase == invertido:
    print('Essa frase \033[1;32mé um palíndromo\033[m')
else:
    print('Essa frase \033[1;31mnão é um palíndromo\033[m')
print(f'Sua frase foi {frase}, e ao contrário ela fica {invertido}')