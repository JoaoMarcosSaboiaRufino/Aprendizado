'''Faça um programa que leia o nome completo de uma pessoa e mostre:
*O nome com todas as letras maiusculas
*O nome com todas as letras minusculas
*Quantas tem no total (sem considerar os espaços)
*Quantas letras tem o primeiro nome'''

nome = input('Digite seu nome completo: ')
dividido = nome.split()
print('seu nome completo em maiusculo é: ', nome.upper())
print('seu nome completo em minusculo é: ', nome.lower())
print(f'Seu nome possui {len(nome.replace(" ", ""))} letras.')
print(f'o seu primeiro nome tem {len(dividido[0])} letras')