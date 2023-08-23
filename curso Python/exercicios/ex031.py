'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
'''

distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor custará R${valor:.2f} reais')
    print('Viagem dentros dos limites.')
else:
    valor = distancia * 0.45
    print(f'O valor custará R${valor:.2f} reais.')
    print('Viagem muita longa.')


