metros = float(input('Digite o valor metrico para a conversão:'))
cm = metros * 100
mm = metros * 1000
km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
print('{}m equivale a {:.0f}cm'.format(metros,cm),'\n{}m equivale a {:.0f}mm'.format(metros,mm),
'\n{}m equivale a {:.0f}km'.format(metros,km),'\n {}m equivale a {:.0f}hm'.format(metros,hm),
'\n{}m equivale a {:.0f}dam'.format(metros,dam))
