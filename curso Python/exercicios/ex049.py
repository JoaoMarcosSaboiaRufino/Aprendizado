'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só
que agora utilizando um laço for.'''
#------------------------------------------------------------------------------------------

tabuada = int(input('Qual número você deseja obter a tabuada? '))

for n in range(0, 11):
    print(f'{tabuada} x {n:2} = {tabuada*n:2}')