#Faça um programa que realize a conversão de graus Celsius para Fahrenheit.

temperatura = float(input('Qual a temperatura local em graus Celsius? '))
c_para_f =  temperatura * 1.8 + 32

print('A temperatura em graus Celsius é {}, e em Fahrenheit é {}.'.format(temperatura, c_para_f))