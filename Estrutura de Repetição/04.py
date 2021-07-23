# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimentode 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programaque calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale apopulação do país B, mantidas as taxas de crescimento.

popuA = 80000
popuB = 200000
anos = 0

while (popuA < popuB):
  anos += 1
  popuA = popuA + (popuA * 0.03)
  popuB = popuB + (popuB * 0.015)
  print('Após ', anos, ' anos', '\nPopulação de A: ', popuA, '\nPopulção de B: ', popuB)