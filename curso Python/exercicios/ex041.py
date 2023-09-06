'''A confederação nacional de natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
*Até 9 anos: MIRIM
*Até 14 anos: INFANTIL
*Até 19 anos:  JUNIOR
*Até 20 anos:  SÊNIOR
*Acima: MASTER'''
#------------------------------------------------------------------------
import datetime
ano_atual = datetime.datetime.today().year

ano_nascimento = input('Qual seu ano de nascimento? ')


if ano_nascimento.isnumeric():

    an = int(ano_nascimento)
    if an > ano_atual or an < 1910:
        print('Data invalida!')
    elif (ano_atual - an) <= 9:
        print('Você está na categoria MIRIM.')
    elif (ano_atual - an) <= 14:
        print('Você está na categoria INFANTIL.')
    elif (ano_atual - an) <= 19:
        print('Você está na categoria JUNIOR.')
    elif (ano_atual - an) <= 20:
        print('Você está na categoria SÊNIOR.')
    else:
        print('Você está na categoria MASTER.')

else:
    print('Não digite letras ou simbolos!')
























