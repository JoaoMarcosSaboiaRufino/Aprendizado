'''Faça um programa que mostre na tela uma contagem regrssiva para o estouro de fogos
de artificio, inde de 10 até 0, com uma pausa de 1 segundo entre eles.'''
#----------------------------------------------------------------------------------------------
from time import sleep

print('VAI COMEÇAR EM... ')

for contagem in range(0, 10):
    print(('='*4) + f'\033[1;36m {contagem} \033[m' + ('='*4))
    sleep(1)

if contagem == 9:

    print('='*4 + '\033[1;36m 10 \033[m' + '='*3)

print('''                                                            ** 
          ________          ____________         ______        ___******   ___
         /    __  \        /            \       |      \      /     **    |   |
        |    |  \  \      /     _____    \      |       \    /      *|    |   |
        |    |__|   |    |     /     \    |     |    |\  \__/  /|    |    |   |
        |    __  __/     |     |     |    |     |    | \      / |    |    |   |
        |    |  \  \     |     \_____/    |     |    |  \____/  |    |    |   |
        |    |   \  |     \              /      |    |          |    |    \ _ /
        |    |___|  |      \            /       |    |          |    |      /|
        |___________/       \__________/        |____|          |____|      \/

''')

