# Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

if n1 > n2 :
  print("Maior: ", n1)
elif n2 < n1 :
  print("Maior: ", n2)
else :
  print("Números iguais!")