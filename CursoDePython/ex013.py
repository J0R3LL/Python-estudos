salario = float(input('Qual o seu salario atual? R$'))
reajuste = salario + (salario*15/100)
print('Seu salario que antes era R${:.2f}, agora com reajuste de 15% a mais passará a receber'
      ' R${:.2f}'.format(salario,reajuste))10