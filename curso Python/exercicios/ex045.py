'''Crie um programa que faça o computador jogar Jokenpô com você.'''
#-------------------------------------------------------------------------------------------------
from random import choice

#modelos

pedra = ('         __  __  __              \n'
         '        /  \/  \/  \  _          \n'
         '        |    |   |   | \         \n'
         '     __ |    |   |   |  |        \n'
         '    |  \/                |       \n'
         '    |                    |       \n'
         '    |                   /        \n'
         '     |_             ___/         \n'
         '       |              |          \n'
         '                                 \n')

tesoura = ('         ___        ____                \n'
           '        |   \      /   /                \n'
           '         \   \    /   /                 \n'
           '          \   \  /   /___  __           \n'
           '        ___\   \/   /    \/  \          \n'
           '       /    \            |    |         \n'
           '       \                      |         \n'
           '        \                    /          \n'
           '         \                  /           \n'
           '          \                 |           \n'
           '           |                |           \n'
           '                                        \n'
           '                                          ')
papel = ('                     __                       \n'
         '                 __ /__\__                    \n'
         '                /--|/_||--\___                \n'
         '               ||_ |   |__|||_\               \n'
         '          ___  |   |   |   |  |               \n'
         '         |__ \ |   |   |   |  |               \n'
         '         |__| \|   |   |   |  |               \n'
         '         |    |    |   |   |  |               \n'
         '         |                     \              \n'
         '          \                    |              \n'
         '           |                  /               \n'
         '            \                /                \n'
         '             \              /                 \n'
         '              |            |                  \n')

#------------------------------------------------------------------------------------------------------------
#parte lógica

conj_jokepo = [pedra, papel, tesoura]
pergunta = (input('Pedra, Papel ou Tesoura? ')).upper()


usuario = 0
computador = choice(conj_jokepo)


if pergunta == 'PEDRA':
    usuario = conj_jokepo[0]
    print(f'Usuário: \n'
          f'{usuario}')
    print(f'Computador: \n'
          f'{computador}')
elif pergunta == 'PAPEL':
    usuario = conj_jokepo[1]
    print(f'Usuário: \n'
          f'{usuario}')
    print(f'Computador: \n'
          f'{computador}')
elif pergunta == 'TESOURA':
    usuario = conj_jokepo[2]
    print(f'Usuário: \n'
          f'{usuario}')
    print(f'Computador: \n'
          f'{computador}')
else:
    print('\033[1;30;41m Erro \033[m')



if usuario == computador:
    print('EMPATE!')
elif usuario == conj_jokepo[0] and computador == conj_jokepo[2]:
    print('\033[1;32;40mO usuário venceu! \033[m')
elif usuario == conj_jokepo[1] and computador == conj_jokepo[0]:
    print('\033[1;32;40mO usuário venceu! \033[m')
elif usuario == conj_jokepo[2] and computador == conj_jokepo[1]:
    print('\033[1;32;40mO usuário venceu! \033[m')
elif computador == conj_jokepo[0] and usuario == conj_jokepo[2]:
    print('\033[1;31;40mO computador venceu! \033[m')
elif computador == conj_jokepo[1] and usuario == conj_jokepo[0]:
    print('\033[1;31;40mO computador venceu! \033[m')
elif computador == conj_jokepo[2] and usuario == conj_jokepo[1]:
    print('\033[1;31;40mO computador venceu! \033[m')






