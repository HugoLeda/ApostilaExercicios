/*
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11%  do  Salário  Bruto,  mas  não  é  descontado  (é  a  empresa  que  deposita).  O  Salário  Líquido  corresponde  ao
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de
horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) ­ isento
Salário Bruto até 1500 (inclusive) ­ desconto de 5%
Salário Bruto até 2500 (inclusive) ­ desconto de 10%
Salário Bruto acima de 2500 ­ desconto de 20% Imprima na tela as informações, dispostas conforme o
exemplo abaixo.
*/

const calculoFolha = (valorHora, qtdHorasTrabalhadas) => {

  if (valorHora <= 0 || qtdHorasTrabalhadas < 0) {
    return 'Dados inconsistentes'
  }


  const totalRendimentos = valorHora * qtdHorasTrabalhadas
  const fgts = totalRendimentos * 0.11
  const valorSindicato = totalRendimentos * 0.03
  const inss = totalRendimentos * 0.1
  
  let ir, irPercentual = 0
  if (totalRendimentos <= 900) {
    ir = 0
  } else if (totalRendimentos > 900 && totalRendimentos <= 1500) {
    ir = totalRendimentos * 0.05 
    irPercentual = 5
  } else if (totalRendimentos > 1500 && totalRendimentos <= 2500) {
    ir = totalRendimentos * 0.1
    irPercentual = 10
  } else {
    ir = totalRendimentos * 0.2
    irPercentual = 20
  }

  const totalDescontos = valorSindicato + ir + inss
  const salLiquido = totalRendimentos - totalDescontos
  const resultado = `
    Salário Bruto: (${valorHora} * ${qtdHorasTrabalhadas}): ${totalRendimentos.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}\n
    ( - ) IR (${irPercentual}%): ${ir.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}\n
    ( - ) INSS (10%): ${inss.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}\n
    FGTS (11%): ${fgts.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}\n
    Total de descontos: ${totalDescontos.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}\n
    Salário Líquido: ${salLiquido.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'})}
  `

  console.log(resultado)
  return resultado
}

calculoFolha(10, 10)