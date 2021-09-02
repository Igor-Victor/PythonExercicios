print('Exercício 50: Programa que leia números 6 numeros inteiros e mostre a soma entre os números pares')
s = 0
for a in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(s)