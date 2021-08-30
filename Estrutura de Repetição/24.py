# Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []

def calcularMedia(notas: list):
  soma = 0
  for i in notas:
    soma += i
  media = round(soma / len(notas), 2)
  return media

resposta = True
while (resposta == True):
  n = float(input('Digite uma nota: '))
  notas.append(n)
  resp = input('Deseja continuar? [S/N]')
  if (resp[0].upper() == 'N'):
    resposta = False

media = calcularMedia(notas)
print(f'A média de {notas} é: {media}')