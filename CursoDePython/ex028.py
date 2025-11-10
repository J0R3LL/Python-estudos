from random import randint
print('Vamos Brincar de adivinhação!!!')
numero = int(input('Digite um número de 0 a 5: '))
sorteado = randint(0,5)
if numero == sorteado:
    print('PARABÉNS VOCÊ ACERTOU!!!')
else:
    print(f'Que pena você errou, o número era {sorteado}, tente novamente!')