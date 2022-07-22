# Escreva um programa que peça o tipo ea quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def valorTotal(tipo, qtd):
  res = 0
  if (qtd <= 5 and qtd > 0):
    if (tipo == 1):
      res = round(qtd * 4.90, 2)
    elif (tipo == 2):
      res = round(qtd * 5.90, 2)
    elif (tipo == 3):
      res = round(qtd * 6.90, 2)
    else:
      res = 'Tipó Inválido'
  elif (qtd > 5):
    if (tipo == 1):
      res = round(qtd * 5.80, 2)
    elif (tipo == 2):
      res = round(qtd * 6.80, 2)
    elif (tipo == 3):
      res = round(qtd * 7.80, 2)
    else:
      res = 'Tipo Inválido'
  return res

def desconto(mtdPgt, valor):
  mtdPgt = mtdPgt.upper()
  if (mtdPgt == 'CARTAO'):
    desconto = valor * 0.05
  else:
    desconto = 0
  return desconto

def gerarNota(tipo, qtd, valorTotal, mtdPgt, desconto):
  nf = open('nf.txt', 'w')
  vr = round(valorTotal - desconto, 2)

  conteudo = list()
  conteudo.append('Hipermercado Tabajara \n')
  conteudo.append('\n')
  conteudo.append('Produto            Qtd             Valor \n')
  conteudo.append(f'{tipo}           {qtd}             {valorTotal} \n')
  conteudo.append('------------------------------------------- \n')
  conteudo.append(f'Método de Pagamento: {mtdPgt} \n')
  conteudo.append(f'Valor do Desconto: R$ {desconto} \n')
  conteudo.append('\n')
  conteudo.append(f'Valor a receber: R$ {vr} \n')

  nf.writelines(conteudo)

def carne(n):
  if (n == 1):
    res = 'Filé Duplo'
  elif (n == 2):
    res = 'Alcatra'
  elif (n == 3):
    res = 'Picanha'
  else:
    res = 'Produto não encontrado'
  return res

tipoCarne = int(input('Carne comprada: \n 1 - Filé Duplo \n 2- Alcatra \n 3 - Picanha: '))
qtd = float(input('Informe a quantidade comprada: '))
mtdPgt = input('Forma de pagamento: ')

vlrTotal = valorTotal(tipoCarne, qtd)
desc = desconto(mtdPgt, vlrTotal)
gerarNota(carne(tipoCarne), qtd, vlrTotal, mtdPgt, desc)