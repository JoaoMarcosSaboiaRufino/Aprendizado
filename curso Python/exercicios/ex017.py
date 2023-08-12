'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente  de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''
import math

#Considere as medidas de comprimento em metros.
cateto_oposto = float(input('Qual o comprimento do cateto oposto? '))
cateto_adjacente = float(input('Qual o comprimento do cateto adjacente? '))

#Primeira forma:
hipotenusa1 = math.sqrt((cateto_oposto**2) + (cateto_adjacente**2))

print('-' * 35)

print(f'Sabendo que o cateto oposto e o adjacente medem respectivamente {cateto_oposto}m e {cateto_adjacente}m, o comprimento da hipotenusa vai ser {hipotenusa1:.2f}m')

#Segunda forma:
hipotenusa2 = (pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)) ** (1/2)

print('-' * 35)

print(f'Sabendo que o cateto oposto e o adjacente medem respectivamente {cateto_oposto}m e {cateto_adjacente}m, o comprimento da hipotenusa vai ser {hipotenusa2:.2f}m')

#Terceira forma:
hipotenusa3 = math.hypot(cateto_oposto, cateto_adjacente)

print('-' * 35)

print(f'sabendo que o cateto oposto e o adjacente medem respectivamente {cateto_oposto}m e {cateto_adjacente}m, o comprimento da hipotenusa vai ser {hipotenusa3:.2f}m')