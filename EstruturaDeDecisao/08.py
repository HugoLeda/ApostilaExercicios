# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo quea decisão é sempre pelo mais barato.

produtos = []

for i in range (3) :
  produto = input("Digite o nome do produto: ")
  valor = float(input("Digite seu valor: "))
  combinacao = {produto : valor}
  produtos.append(combinacao)

print(produtos)