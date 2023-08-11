#Faça um programa que leia o preço de um produto, e mostre o novo preço desse produto com 5% de desconto.

preco_produto = int(input('Qual o preço do produto atualmente? '))
novo_preco = preco_produto - ((preco_produto * 5) / 100)

print('Considerando o preço do produto R${} reais. Com o desconto de 5%, seu novo preço será R${} reais.'.format(preco_produto, novo_preco))