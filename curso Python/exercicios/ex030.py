'''faça uma programa que leia um número inteiro e mostre na tela se ele é impar ou par.'''

n = int(input('Digite um número qualquer: '))
conversao = n % 2
if  conversao == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é impar.'.format(n))