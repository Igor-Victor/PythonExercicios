from time import sleep
print('Exercício 43: Calculador de preço com base em método de pagamento.')
print('Você acabou de comprar um produto de \033[1;32;mR$\033[m300,00. como você gostaria de pagar?: ')
preço = 300.00
desconto10 = preço - preço * 10 // 100
desconto5 = preço - preço * 5 // 100
juros20 = preço + preço * 20 // 100
# TABELA
print('\033[1;34;m-=\033[m' * 20)
print('\033[1;32;m TABELA DE OPÇÕES \033[m')
print('\033[4;31;mA Vista - Dinheiro ou Cheque:\033[m \n 10% de desconto;')
print('\033[4;31;mA Vista - Cartão:\033[m \n 5% de desconto;')
print('\033[4;31;mEm até 2x no cartão:\033[m \n preço normal;')
print('\033[4;31;m3x ou mais no cartão:\033[m \n 20% de juros')
print('\033[1;34;m-=\033[m' * 20)
# TABELA OPÇOES PAGAMENTO
print('\033[1;32;mOPÇÔES - PAGAMENTO\033[m')
print('\033[1m- Dinheiro a vista\n- Cheque a vista\n- Cartão a vista\n- Parcelado 2x no cartão\n- Parcelado 3x no '
      'cartão\033')
print('\033[1;34;m-=\033[m' * 20)
opção = str(input('Como você gostaria de pagar?').strip().lower())
if opção == 'dinheiro a vista':
    print('\033[1;31;mCalculando...\033[m')
    sleep(2)
    print('Você pagará: \033[1;32;mR$\033[m{:.2f} '.format(desconto10))
elif opção == 'cheque a vista':
    print('\033[1;31;mCalculando...\033[m')
    sleep(2)
    print('Você pagará \033[1;32;mR$\033[m{:.2f} '.format(desconto10))
elif opção == 'cartão a vista':
    print('\033[1;31;mCalculando...\033[m')
    sleep(2)
    print('Você pagará: \033[1;32;mR$\033[m{:.2f} '.format(desconto5))
elif opção == 'parcelado 2x no cartão':
    print('\033[1;31;mCalculando...\033[m')
    sleep(2)
    print('Você pagará: \033[1;32;mR$\033[m{:.2f} '.format(preço))
elif opção == 'parcelado 3x no cartão':
    print('\033[1;31;mCalculando...\033[m')
    sleep(2)
    print('Você pagará: \033[1;32;mR$\033[m{:.2f} '.format(juros20))
