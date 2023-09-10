'''Faça um programa que calcule a soma entre todos o números impares que são multiplos
de três e que se encontram no intervalo de 1 até 500'''
#--------------------------------------------------------------------------------------------

soma = 0

for n in range(1, 501, 2):

    if n % 3 == 0:
        soma += n
        print(soma)