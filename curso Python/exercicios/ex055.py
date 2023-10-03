'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menor peso lidor.'''
#----------------------------------------------------------------------------------------------------------

pesos = []

for c in range(0, 5):
    pergunta = float(input('Peso em KG: '))
    pesos.append(pergunta)

pesos.sort()
print(f'Esse foi o maior peso {pesos[4]} Kg')
print(f'Esse foi o menor peso {pesos[0]} Kg')