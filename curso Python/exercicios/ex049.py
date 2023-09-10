'''Desenvolva um programa que leia seis número inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.'''
#----------------------------------------------------------------------------------------

valor = 0

for n in range(0, 6):
    va = int(input('Digite um valor inteiro: '))
    if va % 2 == 0:
        valor += va

print(f'A soma de todos os números pares que você digitou é {valor}')