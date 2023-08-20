'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
separadamente.'''

nome = input('Digite o seu nome completo: ')
nomev2 = nome.split()
repartido = len(nomev2)
print(f'''seu nome completo é: {nome}
seu primeiro nome é: {nomev2[0]}
seu ultimo nome é: {nomev2[len(nomev2) - 1]}''')
