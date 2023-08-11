#Faça um progama que leia um número inteiro, e que mostre o antecessor e o sucessor deste número.

numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1

print('o numero que você escolheu foi {}. o antecessor e o sucessor desse número são respectivamente {} e {}'.format(numero, antecessor, sucessor))