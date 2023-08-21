'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.'''

numero = int(input('Digite um número entre 0 e 9999: ')) / 1000

conversao = str(numero).replace('.', '')

print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(conversao[3], conversao[2], conversao[1], conversao[0]))

#outra forma de fazer:

numero2 = input('Digite um número entre 0 e 9999: ')
conversao1 = (str(int(numero2) / 1000)).replace('.', '')
comprimento = len(conversao1)
unidade = conversao1[comprimento - 1]
dezena = conversao1[comprimento - 2]
centena = conversao1[comprimento - 3]
milhar = conversao1[comprimento - 4]

print('''unidade: {}
dezena:  {}
centena: {}
milhar: {}'''.format(unidade, dezena, centena, milhar))