'''Faça um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
*O primeiro valor é maior
*O segundo valor é maior
*Não existe valor maior, os dois são iguais.'''

n1 = input('\033[1;32;40m Digite um valor: ')
n2 = input('Digite outro valor: \033[m')

conjunto = n1.isnumeric() & n2.isnumeric()

if conjunto == False:
    print('invalido!')
else:
    num1 = int(n1)
    num2 = int(n2)
    print(f'{num1} e {num2}')

    if num1 > num2:
        print('O primeiro número é maior,')
    elif num2 > num1:
        print('O segundo número é maior.')
    else:
        print('Os dois números são iguais.')









