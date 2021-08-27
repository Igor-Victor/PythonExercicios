print('Exercício 42: Calculador de triangulo v2.0')
l1 = int(input('Digite a medida do primeiro lado do seu triângulo? '))
l2 = int(input('Digite a medida do segundo lado do seu triângulo: '))
l3 = int(input('Digite a medida do terceiro lado do seu triãngulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Você pode formar um triãngulo equilátero.')
    if l1 == l2 != l3 != l1:
        print('Você pode formar um triângulo isóceles.')
    elif l1 != l2 != l3:
        print('Você pode formar um triãngulo escaleno.')
else:
    print('Você não pode formar um triângulo com essas retas!')
