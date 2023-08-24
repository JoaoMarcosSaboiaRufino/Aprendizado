'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto ou não.'''

ano = int(input('Digite um ano qualquer: '))

print(f'O ano que você escolheu é {ano}')

if (ano % 4) == 0 :
    print('È um ano bissexto.')
else:
    print('Não é um ano bissexto.')

