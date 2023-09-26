'''Crie um programa que leia uma frase qualquer e diga se ela é um polidromo, desconsiderando
os espaços.
EX:
--APOS A SOPA
--A SACADA DA CASA
--A TORRE DA DERROTA
--O LOBO AMA O BOLO
--ANOTARAM A DATA DA MARATONA'''

frase = str(input('Digite uma frase: '))

frasealt = frase.upper().replace(' ', '')

f_invertido = ''

for cada_letra in frasealt:
    f_invertido = cada_letra + f_invertido

if frasealt == f_invertido:
    print('A frase "{}" é uma FRASE POLIDROMO!'.format(frase))
else:
    print('A frase "{}" não é uma FRASE POLIDROMO!'.format(frase))


