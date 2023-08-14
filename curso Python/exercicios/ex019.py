'''Um professor que sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele,
lendo os nome deles e escrevendo o nome do escolhido.'''
import random

#--------------------------------------------------------------
#Primeira forma de fazer:
alunos = ['joão', 'gabriel', 'ana', 'marcelo', 'fernanda']

aleatório = random.choice(alunos)

print(f'O escolhido para apagar o quadro é o(a)  {aleatório}.')
#--------------------------------------------------------------
print('|' + 35 * '-') #Apenas para separar

#Segunda forma de fazer:
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')

nomes = [nome1, nome2, nome3, nome4]

randomizador = random.choice(nomes)

print(f'O aluno escolhido foi {randomizador}.')









