#Faça um programa que leia um número em metros, e em seguida exibir esse valor convertido para Centimetros e Milimetros

metros = float(input('Quantos metros? '))
centimetros = metros * 100
milimetros = metros * 1000

print('{}m convertido(s) para CM são {:.2f}cm e para MM são {:.2f}mm '.format(metros, centimetros, milimetros))