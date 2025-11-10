numeros = int(input('Digite um número entre 0 e 9999: '))
unidade = numeros // 1 % 10
dezena = numeros // 10 % 10
centena = numeros // 100 % 10
milhar = numeros // 1000 % 10
print(f'Analizando o número {numeros}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')