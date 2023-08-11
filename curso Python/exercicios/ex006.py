#Crie um algoritmo que leia um número, e em seguida mostre o seu: dobro,triplo e raiz quadrada.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2) #Raíz cúbica (1/3) # Raíz quarta (1/4)

print('o dobro de {} é {}. o triplo de {} é {}. E a raiz quadrada de {} é {:.3f}'.format(numero, dobro, numero, triplo, numero, raiz_quadrada))