'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu status, de
acordo com a tabela abaixo:
*Abaixo de 18.5: ABAIXO DO PESO
*Entre 18.5 e 25: PESO IDEAL
*25 até 30: SOBREPESO
*30 até 40:  OBESIDADE
*Acima de 40: OBESIDADE MÓRBIDA
'''
#---------------------------------------------------------------------------------

alturaM = float(input('Qual a sua altura(em metros)? '))
pesoKG = float(input('Qual o seu peso(em kg)? '))

imc = pesoKG / (alturaM ** 2)

print('{:.1f}'.format(imc))

if imc < 18.5:
    print('De acordo com o seu IMC, você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc <= 25:
    print('De acordo com o seu IMC, você está no PESO IDEAL.')
elif imc >= 25 and imc <= 30:
    print('De acordo com o seu IMC, você está no SOBREPESO.')
elif imc >= 30 and imc <= 40:
    print('De acordo com o seu IMC, você está na OBESIDADE.')
else:
    print('De acordo com o seu IMC, você está na OBESIDADE MÓRBIDA.')





