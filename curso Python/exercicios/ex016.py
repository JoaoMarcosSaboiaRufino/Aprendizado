#Faça um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
número = float(input('Digite um número: '))
num_inteiro = math.floor(número)
seg_forma = (math.ceil(número)) - 1

#Primeiro fora de fazer:
print('A parte inteira do número {} é {}'.format(número, num_inteiro))

print('-' * 30)

#Segunda forma de fazer:
print(f'A parte inteira do número {número} é {seg_forma}')
print('-' * 30)

print('-' * 30)

#Terceira forma de fazer:
print('A parte inteira do número {} é {} '.format(número, int(número)))








