'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos de alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle

nome1 = str(input('Qual aluno(a)? '))
nome2 = str(input('Qual aluno(a)? '))
nome3 = str(input('Qual aluno(a)? '))
nome4 = str(input('Qual aluno(a)? '))

alunos = [nome1, nome2, nome3, nome4]
shuffle(alunos)

print(f'Os integrantes do grupo são: {nome1}, {nome2}, {nome3}, {nome4}.'
      f' E a ordem de apresentação será: {alunos[0]}, {alunos[1]}, {alunos[2]}, {alunos[3]}.')




