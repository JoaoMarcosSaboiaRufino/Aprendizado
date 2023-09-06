'''Faça um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
*O primeiro valor é maior
*O segundo valor é maior
*Não existe valor maior, os dois são iguais.'''

n1 = (input('\033[1;32;40m Digite um valor: '))
n2 = (input('Digite outro valor: \033[m'))






cond1 = float(n1) > float(n2)
cond2 = float(n2) > float(n1)
cond3 = float(n1) == float(n2)


if cond1 == True:
    print('O primeiro valor é maior.')
elif cond2 == True:
    print('O segundo valor é maior.')
else:
    print('Os valores são iguais!')




