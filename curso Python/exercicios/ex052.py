'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
#----------------------------------------------------------------------------------------

num = int(input('Digite um número inteiro: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m ', end=' ')
        total += 1
    else:
        print('\033[31m ', end=' ')
    print('{}'.format(c), end=' ')


print('\nO número {} foi divisivel {} vezes.'.format(num, total))

if total == 2:
    print('E por isso ele é um NÚMERO PRIMO!')
else:
    print('\033[31mE por isso ele NÃO é um NÚMERO PRIMO!')