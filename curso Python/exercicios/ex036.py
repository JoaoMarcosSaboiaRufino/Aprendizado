'''Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.
  Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado.'''

print('\033[4;35;40mOlá, bem vindo ao banco!\033[m')

sim_nao = str(input('\033[7;38;44m Você quer um empréstimo? \033[m')).upper()

if sim_nao == 'SIM':
    salario = (float(input('\033[7;38;44m Qual o seu salário? \033[m'))) * 0.3
    ano = int(input('\033[7;38;44m Em quantos pretende pagar? \033[m')) * 12
    imovel = float(input('\033[7;38;44m Qual o valor do imóvel? \033[m'))
    valor_mensal = imovel / ano
    if valor_mensal > salario:
        print('\033[4;30;41m O valor do pagamento mensal excede R${:.2f} reais, oque corresponde a 30% de seu salário! \033[m'.format(salario))
        print('\033[4;30;41m Empréstimo negado! \033[m')
    else:
        print('\033[130;42m ;Empréstimo liberado! \033[m')
else:
    print('\033[4;35;40m Tenha um ótimo dia! \033[m')

