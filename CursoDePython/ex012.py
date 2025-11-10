produto = float(input('Qual o valor do produto a ser descontado? R$'))
desconto = produto-(produto*5/100)
print('O produto que custava R${:.2f}, agora com desconto de 5% custa R${:.2f}'.format(produto,desconto))