# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programapara que ele mostre os números um ao lado do outro.

n = []

for i in range(1, 21, 1):
  n.append(i)
  print(i)

print(n)