'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram paradesenvolver o programa que calculará os reajustes. Faça  um  programa  que  recebe  o  salário  de  um  colaborador  e  o  reajuste  segundo  o  seguinte  critério, baseado no salário atual: 
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:o salário antes do reajuste;o percentual de aumento aplicado;o valor do aumento;o novo salário, após o aumento.
'''

def aumento(sal: float):
  aumento = 0
  pct = 0
  if (sal <= 280):
    pct = 20    
  elif (sal > 280 & sal <= 700):
    pct = 15
  elif (sal > 700 & sal <= 1500):
    pct = 10
  elif (sal > 1500):
    pct = 5
  else:
    return ('Salário inválido!')

  aumento = (sal / 100) * pct
  novoSal = sal + aumento

  return {"salBase": sal, "pctAumento": pct, "valorAumento": aumento, "novoSal": novoSal}

salario = float(input('Digite o salario a ser calculado o aumento: R$ '))
res = aumento(salario)
print(res)