print('Exercício 42: Calculador de triangulo v2.0')
l1 = int(input('Digite a medida do primeiro lado do seu triângulo? '))
l2 = int(input('Digite a medida do segundo lado do seu triângulo: '))
l3 = int(input('Digite a medida do terceiro lado do seu triãngulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Você pode formar um triângulo com essas medidas!')
elif l1 == l2 and l1 == l3 or l2 == l1 and l2 == l3 or l3 == l1 and l3 == l2:
    print('Você pode formar um triângulo equilátero!')
elif l1 == l2 and l1 != l3 or l2 == l1 and l2 != l3 or l3 == l1 and l3 != l2:
    print('Você pode formar um triãngulo isóceles!')
elif l1 != l2 and l1 != l3 or l2 != l1 and l2 != l3 or l3 != l1 and l3 != l2:
    print('Você pode formar um triâgulo escaleno!')
else:
    print('Você não pode formar um triângulo com essas retas!')
