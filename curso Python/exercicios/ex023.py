'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.'''

numero = int(input('Digite um número entre 0 e 9999: '))

if numero > 9999 :
    print('Erro, limite de quatro digitos')
else:
    convertido = str(numero)
    print(f"""o número é: {numero}
    Unidade {convertido[3]}
    Dezena {convertido[2]}
    Centena {convertido[1]}
    Milhar {convertido[0]}""")

