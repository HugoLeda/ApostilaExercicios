# Faça um Programa que leia três números e mostre o maior e o menor deles.

numeros = []

for i in range (3) :
  numeros.append(float(input("Digite um número: ")))

print(min(numeros, key = float)) # min restorna o menor valor de uma lista