'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
CONSIDERANDO A MAIORIDADE COMO 21 ANOS.'''
#-------------------------------------------------------------------------------------------------
import datetime

ano_atual = datetime.date.today().year

contador = 0

for c in range(1,8):
    idade = int(input('Em qual ano você nasceu? '))
    print(ano_atual-idade, 'anos')
    if ano_atual-idade >= 21:
        contador += 1

print(f'De acordo com as datas de nascimento fornecidas, {contador} pessoa(s) jáo são de maioridade e {7 - contador} pessoa(s) ainda não.')