# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Validea entrada e permita repetir a operação.

popuA = int(input('Informe a menor população para A: '))
taxaA = float(input('Taxa de cresmento de A em %: '))
taxaA = taxaA/100

popuB = int(input('Informe a menor população para B: '))
taxaB = float(input('Taxa de cresmento de B em %: '))
taxaB = taxaB/100

anos = 0

if (taxaA > taxaB):
  while (popuA < popuB):
    anos += 1
    popuA = popuA + (popuA * taxaA)
    popuB = popuB + (popuB * taxaB)
    print('Após ', anos, ' anos', '\nPopulação de A: ', popuA, '\nPopulção de B: ', popuB)
else:
  print('A nunca ultrapassará a população de B, pois sua taxa de crescimente e número de habitantes são menores')