'''Desenvolva um programq que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''

import time

reta_1 = float(input('Qual é o valor da primeira reta? '))
reta_2 = float(input('Qual é o valor da segunda reta? '))
reta_3 = float(input('Qual é valor da terceira reta? '))


print('\033[0;31mPROCESSANDO...\033[m')

time.sleep(3)
if (reta_1 > reta_2) & (reta_1 > reta_3):
    value = reta_3 + reta_2
    if value > reta_1:
        print(' {}Sim, é possivel formar um triângulo.{}'.format('\033[1;32m', '\033[m'))
    else:
        print(' {}Não é possivel formar um triãngulo.{}'.format('\033[1;33m', '\033[m'))

if (reta_2 > reta_1) & (reta_2 > reta_3):
    value = reta_1 + reta_2
    if value > reta_2:
        print(' {}Sim, é possivel formar um triângulo.{}'.format('\033[1;32m', '\033[m'))
    else:
        print(' {}Não é possivel formar um triângulo.{}'.format('\033[1;33m', '\033[m'))

if (reta_3 > reta_1) & (reta_3 > reta_2):
    value = reta_1 + reta_2
    if value > reta_3:
        print(' {}Sim, é possivel formar um triângulo.{}'.format('\033[1;32m', '\033[m'))
    else:
        print(' {}Não é possivel formar um triângulo.{}'.format('\033[1;33m', '\033[m'))