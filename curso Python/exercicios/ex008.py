#Faça um programa que leia um número em metros, e em seguida exibir esse valor convertido para Centimetros e Milimetros

metros = float(input('Quantos metros? '))
cm = metros * 100
mm = metros * 1000
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000

print(f' {metros}m para mm, vão ser {mm}mm \n {metros}m para cm, vão ser {cm}cm \n {metros}m para dm, vão ser {dm}dm \n'
      f' {metros}m para dam, vão ser {dam}dam \n {metros}m para hm, vão ser {hm}hm \n {metros}m para km, vão ser {km}km')