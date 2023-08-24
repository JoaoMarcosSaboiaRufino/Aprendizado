'''Escreva um programa que pergunta o salário de um funcionario e calcule o valor de seu aumento.
*Para salários superiores a R$1250,00 calcule um aumento de 10%.
*Para os inferiores ou iguais , o aumento é de 15%.'''

salario = float(input('Qual o seu salário? '))

sit1 = salario > 1250
sit2 = salario <= 1250

if sit1 == True:
    novo_salario = salario * 10 / 100 + salario
    print(f'Seu novo salário será de R${novo_salario:.2f} reais. (Su)')
if sit2 == True:
    novo_salario = salario * 15 / 100 + salario
    print(f'Seu novo salário será de R${novo_salario:.2f} reais. (In)')
