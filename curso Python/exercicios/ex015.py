#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

dias_alugado = float(input('Quantos dias esse carro foi alugado? '))
km_rodados = float(input('Quantos km esse carro rodou enquanto estava alugado?'))
preco_a_pagar =  (dias_alugado * 60) + (km_rodados * 0.15)

print('Considerando que o carro foi alugado por {} dias, e rodou {}km. O preço a pagar será de R${:.2f} por tudo.'.format(dias_alugado, km_rodados, preco_a_pagar))
