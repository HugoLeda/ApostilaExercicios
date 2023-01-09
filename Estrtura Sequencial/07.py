# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

def areaQuadrado(lado):
  return lado * lado

lado = float(input("Digite o tamanho do lado do quadro: "))
area = areaQuadrado(lado)
dobroArea = area * 2

print("O dobro da área do quadrado é: ", dobroArea)