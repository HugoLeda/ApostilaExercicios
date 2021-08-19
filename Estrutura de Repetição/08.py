# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
soma = 0

for i in range(5):
  n = float(input('Informe um número: '))
  numeros.append(n)
  soma += n

media = soma / 5
print(f'Soma: {soma}, \nMédia: {media}')