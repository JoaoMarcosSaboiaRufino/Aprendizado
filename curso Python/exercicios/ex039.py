'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acrodo com sua idade:
*Se ele ainda vai ser se alistar ao serviço militar
*Se é a hora de se alistar
*Se já passou do tempo de alistamento
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime

data = datetime.date.today()
conv = (str(data).replace('-', ' ')).split()
ano_atual = int(conv[0])
#---------------------------------------------------
ano_nascimento = int(input('Em qual ano você nasceu? '))

if ano_nascimento > ano_atual or ano_nascimento < 1910:
    print('Como assim?! ´-´')
else:
    if (ano_atual - ano_nascimento) == 18:
        print('Está na hora de se alistar!')
    elif (ano_atual - ano_nascimento) < 18:
        print('Você ainda vai se alistar.')
        print(f'Faltam {18 - (ano_atual - ano_nascimento)} ano(s) para você se alistar!')
    else:
        print('Já passou o tempo de seu alistamento.')
        print(f'Se passaram {18 - (ano_atual - ano_nascimento)} ano(s)')




