# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite uma nota entre 0 e 10: '))
executar = True

while executar:
  if (nota >= 0) & (nota <= 10):
    print('Nota válida, está entre 0 e 10!')
    executar = False
  else:
    print('Valor Inválido!')
    nota = float(input('\nDigite uma nota entre 0 e 10: '))