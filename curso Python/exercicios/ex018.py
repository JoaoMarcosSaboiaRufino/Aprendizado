'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math

valor = math.radians(float(input('Digite um valor: ')))
seno = math.sin(valor)
cosseno = math.cos(valor)
tangente = math.tan(valor)

print(f'O valor do SENO é {seno} \n'
      f'O valor do COSSENO é {cosseno} \n'
      f'O valor do TANGENTE é {tangente}')