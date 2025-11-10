viagem = float(input('Quantos Km de distância tem sua viagem?: '))
if viagem <= 200 :
    print(f'O preço da viagem será R${viagem * 0.50:.2f}')
else:
    print(f'O preço da viagem será R${viagem * 0.45:.2f}')