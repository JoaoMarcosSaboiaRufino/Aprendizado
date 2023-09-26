'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
#----------------------------------------------------------------------------------------

numero = int(input('Digite um número inteiro: '))
total = 0

cores = ['\033[32m', '\033[31m']

for nums in range(1, numero + 1):
    if numero % nums == 0:
        print(cores[0], end='')
        total += 1
    else:
        print(cores[1], end='')
    print(nums, end=' ')

print('\nO número {} foi divisivel {} vezes.'.format(numero, total))

if total == 2:
    print('E por isso ele é um NÚMERO PRIMO!')
else:
    print('\033[31mE por isso ele NÃO é um NÚMERO PRIMO!')












