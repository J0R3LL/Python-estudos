km = float(input('Quantos km rodados?'))
dias = int(input('Por quantos dias foi alugado?'))
total = float(60 * dias) + (0.15 * km)
print('Total a ser pago é R${:.2f}'.format(total))