from math import hypot
b = int(input('Digite o comprimento cateto oposto: '))
c = int(input('Digite o comprimento cateto adjacente: '))
a = hypot(b,c)
print('A a hipotenusa desse triângulo é {:.2f}'.format(a))
