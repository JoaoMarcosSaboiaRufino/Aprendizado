'''Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário perdeu ou não.'''

import random

numerorandom = random.randint(0, 5)
print('Pensei em um número entre 0 e 5. Você pode adivinhar? ')

numerochutado = int(input('Chutar: '))

if(numerochutado == numerorandom):
    print('Você acertou o número.')
else:
    print('Você errou o número. Eu pensei em {}.'.format(numerorandom))

