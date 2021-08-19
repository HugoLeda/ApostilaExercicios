# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

impares = []

for i in range(1, 51, 1):
  resto = i % 2
  if (resto != 0):
    impares.append(i)

print(impares)