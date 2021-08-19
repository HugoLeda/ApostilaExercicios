# Faça um programa que leia 5 números e informe o maior número.

numeros = []
for i in range(5):
  n = float(input('Informe um número: '))
  numeros.append(n)

print(max(numeros))