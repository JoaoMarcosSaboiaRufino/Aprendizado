'''Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
*À vista dinheiro: 10% DE DESCONTO
*À vista no cartão: 5% DE DESCONTO
*Em até 2x no cartão: PREÇO NORMAL
*3x ou mais no cartão: 20% DE JUROS
'''
#-----------------------------------------------------------------------------------
from time import sleep

preco = input('Qual o preço do produto? ')
print('E qual forma de pagamento você deseja? '
      '\n \033[1;36;40mDinheiro/Cheque: \033[m'
      '\n\033[0;30;44m  *À vista com 10% de desconto. MÉTODO 1\033[m' 
      '\n \033[1;36;40mCartão: \033[m'
      '\n\033[0;30;44m  *À vista no cartão com 5% de desconto. MÉTODO 2'
      '\n  *Em até 2x no cartão pelo preço normal. MÉTODO 3'
      '\n  *3x ou mais no cartão com 20% de juros. MÉTODO 4\033[m')

met = (input('Qual método de pagamento você quer?(seleciona pela numeração do método) '))

#verificações
verif = preco.isnumeric()
verif2 = '.' in preco
other_verif = met.isnumeric() and int(met) < 5


if verif == True or verif2 == True:

    if other_verif == True:
        metint = int(met)
        preconew = float(preco)
        print(metint)
#------------------------------------------------------------------------------------------------------------|
#METODO 1

        if metint == 1:
            novo_preco = preconew - (preconew * 0.1)
            escolha = str(input(f'Será cobrado R${novo_preco:.2f} reais. Deseja confirmar a compra?'
                                f'\n Sim ou Não? '))
            escolhamod = escolha.upper()

            if escolhamod == 'SIM': #ESCOLHA SIM
                tempo = '\033[1;31mAGUARDE.'
                print(tempo)
                sleep(0.5)
                tempo = 'AGUARDE..'
                print(tempo)
                sleep(0.5)
                tempo = 'AGUARDE... \033[m'
                print(tempo)
                sleep(2)
                print('\033[1;32m Compra finalizada! \033[m')

            elif escolhamod == 'NÃO' or escolhamod == 'NAO': #ESCOLHA NÃO
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;33m Compra cancelada pelo usuário! \033[m')

            else:
                print('\033[1;41;30m Resposta inválida! \033[m') #RESPOSTA QUE NÃO SEJA 'NÃO' OU 'SIM'

#------------------------------------------------------------------------------------------------------------|
#MÉTODO 2

        elif metint == 2:
            novo_preco = preconew - (preconew * 0.05)
            escolha = str(input(f'Será cobrado R${novo_preco:.2f} reais. Deseja confirmar a compra? '
                                '\n Sim ou Não? '))
            escolhamod = escolha.upper()

            if escolhamod == 'SIM': #ESCOLHA SIM
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;32m Compra finalizada! \033[m')

            elif escolhamod == 'NAO' or escolhamod == 'NÂO': #ESCOLHA NÃO
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;33m Compra cancelada pelo usuário! \033[m')

            else:
                print('\033[1;30;41m Resposta inválida! \033[m') #RESPOSTA QUE NÃO SEJA 'NÃO' OU 'SIM'

#------------------------------------------------------------------------------------------------------------|
#MÉTODO 3

        elif metint == 3:
            preco_parcelado2x = preconew / 2
            escolha = str(input(f'Será cobrado duas parcelas de R${preco_parcelado2x:.2f} reais. Deseja confirmar a compra?'
                                f'\n Sim ou Não? '))
            escolhamod = escolha.upper()

            if escolhamod == 'SIM': #ESCOLHA SIM
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;32m Compra finalizada! \033[m')

            elif escolhamod == 'NÃO' or escolhamod == 'NAO': #ESCOLHA NÃO
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;33m Compra cancelada pelo usuário! \033[m')

            else:
                print('\033[1;30;41m Resposta inválida! \033[m')#RESPOSTA QUE NÃO SEJA 'NÃO' OU 'SIM'

#------------------------------------------------------------------------------------------------------------|
#MÉTODO 4

        elif metint == 4:
            novo_preco = (preconew + (preconew * 0.2)) / 3
            escolha = str(input(f'Será cobrado R${novo_preco:.2f} reais por cada parcela. Deseja confirmar a compra? '
                                '\n Sim ou Não? '))
            escolhamod = escolha.upper()


            if escolhamod == 'SIM':#ESCOLHA SIM
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;32m Compra finalizada! \033[m')

            elif escolhamod == 'NÃO' or escolhamod == 'NAO': #ESCOLHA NÃO
                print('\033[1;31mAGUARDE.')
                sleep(0.5)
                print('AGUARDE..')
                sleep(0.5)
                print('AGUARDE... \033[m')
                sleep(2)
                print('\033[1;33m Compra cancelada pelo usuário! \033[m')
            else:
                print('\033[1;30;41m Resposta inválida! \033[')

    else:
        print('\033[1;31m Esse método não existe. \033[m')

else:
    print('\033[1;31m Erro \033[m')












