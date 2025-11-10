import random
aluno1 = input('Digite o nome do primeiro(a) aluno(a): ')
aluno2 = input('Digite o nome do segundo(a) aluno(a): ')
aluno3 = input('Digite o nome do terceiro(a) aluno(a): ')
aluno4 = input('Digite o nome do quarto(a) aluno(a): ')
lista = [aluno4,aluno3,aluno1,aluno2]
sorteio = random.choice(lista)
print ('Dos quatro alunos sorteados o escolhido foi {}.'.format(sorteio))
