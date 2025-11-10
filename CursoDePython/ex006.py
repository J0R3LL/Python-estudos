import math
numero = int(input('Digite um número:'))
dobro = numero * 2
triplo = numero * 3
raiz =  math.sqrt(numero)
print('O dobro de {} é: {}'.format(numero,dobro),'\nO triplo de {} é: {}'.format(numero,triplo),
      '\nA raiz quadrada de {} é: {:.2f}'.format(numero,raiz))
