'''Escreva um programa que leia um número inteiro qualquer número inteiro
e peça para o usuário escolher qual será a base de conversão:
* 1 para BINÁRIO
* 2 para OCTAL
* 3 para HEXADECIMAL
'''
#----------------------------------------------------------------------------------------------------------------[
inte = int(input('Digite qualquer número inteiro: '))
base = int(input('''Escolha a base de conversão que deseja:
*BINÁRIO --> [1]
*OCTAL --> [2]
*HEXADECIMAL --> [3]
'''))

if base == 1:
    print('O número {} convertido para BINÁRIO é: {}'.format(inte, bin(inte)[2:]))
elif base == 2:
    print('O número {} convertido para OCTAL é: {}'. format(inte, oct(inte)[2:]))
elif base == 3:
    print('O número {} convertido para HEXADECIMAL é: {}'.format(inte, hex(inte)[2:]))













