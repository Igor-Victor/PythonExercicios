print('Exercício 52: Programa que diz o primeiro termo de uma P.A e a sua razão e depois  mostre os 10 primeiros termos')
print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('=' * 30)
primeirotermo = int(input('Insira o Primeiro Termo: '))
razao = int(input('Insira a Razão: '))
pa = primeirotermo + (10 - 1) * razao
for i in range(primeirotermo, pa + razao, razao):
    print(f'{i}', end='→ ')
print('\033[1;31;mFinalizado!\033[1;m')
