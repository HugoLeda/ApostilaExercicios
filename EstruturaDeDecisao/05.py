# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;A mensagem "Reprovado", se a média for menor do que sete;A mensagem "Aprovado com Distinção", se a média for igual a dez

def validarMedia(n1, n2) :
  
  if (n1 < 0 or n1 > 0 or n2 < 0 or n2 > 10) :
    return "Notas inválidas"

  media = (n1 + n2) / 2
  
  if (media == 10) :
    res = "Aprovado com Distinção"
  elif (media >= 7) :
    res = "Aprovado"
  else :
    res = "Reprovado"

  return res

n1 = float(input("Digita a nota 1: "))
n2 = float(input("Digita a nota 2: "))

situacao = validarMedia(n1, n2)

print("Aluno ", situacao)