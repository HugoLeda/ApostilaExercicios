# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo quea decisão é sempre pelo mais barato.

menorValor = 1000000
produtoFinal = ''

for i in range(3) :
  produto = input("Digite o nome do produto: ")
  valor = float(input("Digite seu valor: "))
  if (valor < menorValor) :
    menorValor = valor
    produtoFinal = produto

print('Você deve comprar ' + produtoFinal + ' pois é o mais barato, custando R$ ', menorValor)