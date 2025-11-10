primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
minimo = min(primeiro,segundo,terceiro)
maximo = max(primeiro,segundo,terceiro)
if primeiro > segundo and primeiro > terceiro :
    print(f'O maior valor digitado foi {maximo}')
if segundo > primeiro and segundo > terceiro :
    print(f'O maior numero digitado foi {maximo}')

if terceiro > primeiro and terceiro > segundo :
    print(f'O maior numero digitado foi {maximo}')
if segundo == primeiro == terceiro :
    print('Todos os números são iguais!')
else:
    print(f'O menor numero digitado foi {minimo}')