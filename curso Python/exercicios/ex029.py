'''Faça um programa que leia a velocidade de um carro pelo teclado. Se ele ultrapassar 80km/h, mostre uma
mensagem dizendo que ele foi multado.
  A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual é a velocidade do carro? '))

if velocidade > 80:
    print('Você ultrapassou os limites de velocidade, e será multado.!')
    print('Você atingiu a velocidade de {}km/h. Sua multa custará R${:.2f} reais'.format(velocidade, (velocidade-80)*7))



