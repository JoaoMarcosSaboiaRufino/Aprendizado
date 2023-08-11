#Faça um programa que leia as duas notas de um aluno, e calcule a sua média

nota_1 = int(input('Qual sua primeira nota? '))
nota_2 = int(input('qual sua segunda nota? '))
nota_media = (nota_1+nota_2) / 2

print("Sua primeira e segunda nota são {} e {}. Portanto sua nota média é {}". format(nota_1, nota_2, nota_media))
