# -*- coding: latin1 -*-

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

import math
if a > (b + c):
    print ('Se A > B + C nao formam triangulo algum, se A eh o maior')
else:
    perim = (a + b + c) / 2
    area = perim * (perim - a) * (perim - b) * (perim - c)
    areaF = math.sqrt(area)
    print('A area do triangulo eh : %f' % areaF)

