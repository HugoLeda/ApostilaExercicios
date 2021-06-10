# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ('A', 'E', 'I', 'O', 'U')

letra = str(input("Digite uma letra: "))
letra = letra.upper()

res = "Consoante!"
for vogal in vogais :
  if (letra == vogal) :
    res = "Vogal!"

print(res)