#Faça um programa que leia o nome de uma cidade, e se essa cidade começa ou não com "SANTOS".

msg = input('Digite o nome de uma cidade: ')
fatiada = msg.split()
print('SANTO' in fatiada[0])