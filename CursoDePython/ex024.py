#nome = str(input('Digite o nome da cidade: '))
#nome = nome.capitalize()
#nome = nome.replace('santo','Santo')
#nome = (nome.strip())
#santo = 'Santo'in nome
#primeirosanto = 'Santo'in nome[:5]

#print(f'{nome} possui o nome santo?: {santo}')
#print(f'{nome} começa com o nome santo?:{primeirosanto}')

cidade = str(input('Em que cidade você nasceu:')).strip()
print(cidade[:5].upper() == 'SANTO')