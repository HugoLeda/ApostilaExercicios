# Faça um programa que leia e valide as seguintes informações: a. Nome: maior que 3 caracteres;b. Idade: entre 0 e 150;c. Salário: maior que zero;d. Sexo: 'f' ou 'm';e. Estado Civil: 's', 'c', 'v', 'd';

def validarNome(n: str):
  if (len(n) > 3):
    return [True, 'Nome válido!']
  else:
    return [False, 'Nome inválido!']

def validarIdade(i: int):
  if (i >= 0 and i <= 150):
    return [True, 'Idade válida!']
  else:
    return [False, 'Idade inválida!']
  
def validarSalario(s: float):
  if (s > 0):
    return [True, 'Salário válido!']
  else:
    return [False, 'Salário inválido!']

def validarSexo(s: str):
  s = s.lower()
  if (s[0] == 'f' or s[0] == 'm'):
    return [True, 'Sexo válido!']
  else:
    return [False, 'Sexo inválido!']

def validarEsCivil(ec: str):
  ec = ec.lower()
  if (ec[0] == 's' or ec[0] == 'c' or ec[0] == 'v' or ec[0] == 'd'):
    return [True, 'Estado Civil Válido!']
  else:
    return [False, 'Estado Civil inválido']

def inserirDados():
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))
  salario = float(input('Digite o salário: R$ '))
  sexo = input('Digite o sexo: ')
  esCivil = input('Digite o Estado Civil: ')

  vnome = validarNome(nome)
  vidade = validarIdade(idade)
  vsalario = validarSalario(salario)
  vsexo = validarSexo(sexo)
  vesCivil = validarEsCivil(esCivil)

  print(vnome[1] + '\n' + vidade[1] + '\n' + vsalario[1] + '\n' + vsexo[1] + '\n' + vesCivil[1])

inserirDados()