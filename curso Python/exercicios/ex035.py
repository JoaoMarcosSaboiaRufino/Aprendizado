'''Desenvolva um programq que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''

reta_1 = float(input('Qual é o valor da primeira reta? '))
reta_2 = float(input('Qual é o valor da segunda reta? '))
reta_3 = float(input('Qual é valor da terceira reta? '))

if (reta_1 > reta_2) & (reta_1 > reta_3):
    value = reta_3 + reta_2
    if value > reta_1:
        print('Sim, é possivel formar um triângulo.')
    else:
        print('Não é possivel formar um triãngulo.')

if (reta_2 > reta_1) & (reta_2 > reta_3):
    value = reta_1 + reta_2
    if value > reta_2:
        print('Sim, é possivel formar um triângulo.')
    else:
        print('Não é possivel formar um triângulo.')

if (reta_3 > reta_1) & (reta_3 > reta_2):
    value = reta_1 + reta_2
    if value > reta_3:
        print('Sim, é possivel formar um triângulo.')
    else:
        print('Não é possivel formar um triângulo.')