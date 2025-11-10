frase = str(input('Digite seu nome completo: '))
caps = frase.upper()
minus = frase.lower()
divisao = frase.split()
junta = ''.join(divisao)
total = len(junta)
primeiro = len(divisao[0])
print('Nome completo em maiúsculo: {} \n''Nome completo em Minúsculo: {}\n''Total de letras ao todo é: {} letras\n'''
      'O primeiro nome é {} e contém: {} letras'
      .format(caps,minus,total,divisao[0],primeiro))