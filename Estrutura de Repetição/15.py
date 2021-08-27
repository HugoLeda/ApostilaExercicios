# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

fibonacci = [1, 1]

n = 1000
while (fibonacci[len(fibonacci) - 1] < n):
  print(fibonacci)
  nAdd = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
  if (nAdd < n):
    fibonacci.append(nAdd)

print(fibonacci)