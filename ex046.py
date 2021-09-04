from time import sleep
import emoji
print('Exercício 46: contagem regressiva de 10 até 0 com inervalo de 10 segundos')
regressivo = 10
print('Bem Vindo ao Reveillon! Os fogos começam em 10 segundos!')
sleep(1)
for regressivo in range(10, -1, -1):
    print(regressivo)
    sleep(1)
print(emoji.emojize(':collision:', use_aliases=True))
