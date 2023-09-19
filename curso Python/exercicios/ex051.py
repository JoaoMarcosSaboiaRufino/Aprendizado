'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progessão.'''
#---------------------------------------------------------------------------------------------------

razao = int(input('Razão(r): '))
primeiro_termo = int(input('primeiro termo: '))




for c in range(primeiro_termo, (primeiro_termo + ((10 - 1) * razao))+1, razao):
   print(c)








