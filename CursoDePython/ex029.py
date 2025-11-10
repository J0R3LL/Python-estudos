km = int(input('Quantos Km está marcando?: '))
multa = (km-80)*7
if km > 80:
    print(f'Multado por exceder o limite da via 80Km/h!, valor da multa:R${multa:.2f}')
else:
    print('Dentro do limite da via!')
print('Dirija com segurança!')