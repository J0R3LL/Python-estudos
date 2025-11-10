import math
angulo = int(input('Digite o ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O ângulo de {}º\n tem seno de {:.2f}\n cosseno {:.2f}\n tangente de {:.2f}'.format(angulo,sen,cos,tg))