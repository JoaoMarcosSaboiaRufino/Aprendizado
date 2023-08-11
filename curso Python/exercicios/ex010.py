#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira, e quantos dolares ela pode comprar
#considerando US$1,0 = R$3,27

dinheiro = int(input('Quarto dinheiro você tem na carteira? '))
vai_comprar = dinheiro / 3.27

print('Com R${} rais, você vai poder comprar US${:.2f} dolares'.format(dinheiro, vai_comprar))
