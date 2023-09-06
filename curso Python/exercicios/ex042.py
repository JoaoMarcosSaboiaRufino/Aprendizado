'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
*EQUILÁTERO = todos os lados iguais
*ISÓSCELES = dois lados iguais
*ESCALENO = todos os lados diferentes.'''
#-----------------------------------------------------------------------
reta1 = float(input('Valor da primeira reta: '))
reta2 = float(input('Valor da segunda reta: '))
reta3 = float(input('Valor da terceira reta: '))

r1maior = reta1 > reta2 and reta1 > reta3
r2maior = reta2 > reta1 and reta2 > reta3
r3maior = reta3 > reta1 and reta3 > reta2

condequi = reta1 == reta2 and reta2 == reta3 and reta3 == reta1
condisos = (reta1 == reta2 and reta1 != reta3 or reta1 == reta3 and reta1 != reta2
            or reta2 == reta1 and reta2 != reta3 or reta2 == reta3 and reta2 != reta1
            or reta3 == reta1 and reta3 != reta2 or reta3 == reta2 and reta3 != reta1)
condesca = (reta1 != reta2 and reta1 != reta3 and reta2 != reta1 and reta2 != reta3 and reta3 != reta1
            and reta3 != reta2)

if r1maior == True:
    verificacao = (reta2 + reta3) > reta1
    if verificacao == True:
        print('È possivel formar um Triângulo.')
        print('-' * 35)
        if condequi == True:
            print('È possivel formar um triângulo EQUILÁTERO!')
        elif condisos == True:
            print('È possivel formar um triângulo ISÓSCELES!')
        elif condesca == True:
            print('È possivel formar um triângulo ESCALENO!')
    else:
        print('Não é possivel formar um triângulo')

elif r2maior == True:
    verificacao = (reta1 + reta3) > reta2
    if verificacao == True:
        print('È possivel formar um Triângulo.')
        print('-' * 35)
        if condequi == True:
            print('È possivel formar um triângulo EQUILÁTERO!')
        elif condisos == True:
            print('È possivel formar um triângulo ISÓSCELES!')
        elif condesca == True:
            print('È possivel formar um triângulo ESCALENO!')
    else:
        print('Não é possivel formar um triângulo')

else:
    verificacao = (reta1 + reta2) > reta3
    if verificacao == True:
        print('È possivel formar um Triângulo.')
        print('-' * 35)
        if condequi == True:
            print('È possivel formar um triângulo EQUILÁTERO!')
        elif condisos == True:
            print('È possivel formar um triângulo ISÓSCELES!')
        elif condesca == True:
            print('È possivel formar um triângulo ESCALENO!')
    else:
        print('Não é possivel formar um triângulo')















