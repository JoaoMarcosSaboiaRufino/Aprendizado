#Faça um algoritmo que leia o salário de um funcionario e mostre novo salário, com 15% de aumento.

salario_antigo = int(input('Quanto é seu salário? '))
novo_salario = (salario_antigo * 15 / 100) + salario_antigo

print('Considerando seu salario antigo como R${} reais, seu novo salário com o aumento de 15% será R${} reais.'.format(salario_antigo, novo_salario))