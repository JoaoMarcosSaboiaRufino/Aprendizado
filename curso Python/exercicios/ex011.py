#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2m*2.

largura = int(input('Qual a largura da parede? '))
altura = int(input('Qual a altura da parede? '))
area = largura * altura
litros_de_tinta = area / 2

print('Com a largura da perede sendo {}m e sua altura sendo {}m, então sua área será de {}m². '
      'Nesse caso serão necessários {} litros de tinta para pintá-la'.format(largura, altura, area, litros_de_tinta))
