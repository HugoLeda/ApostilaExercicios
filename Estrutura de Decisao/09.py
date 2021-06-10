# Faça um Programa que leia três números e mostre­os em ordem decrescente.

numeros = []

for i in range(3) :
  numero = float(input('Digite um número: '))
  numeros.append(numero)

numeros.sort(key = float, reverse = True)
print(numeros)