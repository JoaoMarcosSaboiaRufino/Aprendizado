'''Faça um programa que leia uma frase pelo teclado e mostre:
*identifique quantos 'R' tem na frase
*identifique a posição do primeiro 'R'
*identifique a posição do ultimo 'R'
'''

frase = str(input('Digite uma frase: '))
print('A frase tem {} R'.format((frase.upper()).count('R')))
print('A frase tem o primeiro R na posição {}'.format(frase.upper().find('R') + 1))
print('A frase tem seu ultimo R na posiçao {}'.format(frase.upper().rfind('R') + 1))


