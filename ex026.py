print('Exercício26: Analisador de frase')
frase = str(input('Digite uma frase: ')).strip().lower()
# Quantas vezes aparece a letra A
print('A letra "A" aparece na frase {} vezes. '.format(frase.count('a')))
print('A letra "A" aparece primeiro na posição {}. '.format(frase.find('a')+1))
print('A letra "A" aparece por último na posição {}. '.format(frase.rfind('a')+1))
