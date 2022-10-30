/*
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
  a.  Álcool:
    b.  até 20 litros, desconto de 3% por litro
    c.  acima de 20 litros, desconto de 5% por litro
  d.  Gasolina:
    e.  até 20 litros, desconto de 4% por litro
    f.  acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A­ álcool, G­ gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo­se que o preço do litro da gasolina é R$ 5,02 o preço do litro do álcool é R$ 4,70.
*/

function valorPagar(tipo, litros) {
  const precoGasolina = 5.02
  const precoAlcool = 4.70
  let valorTotal
  let valorDesconto
  
  if (litros < 0) {
    return "Quantidade de litros inválida!"
  }
  if (tipo.toUpperCase() === "A") {
    if (litros <= 20) {
      valorDesconto = litros * precoAlcool * 0.03
    } else {
      valorDesconto = litros * precoAlcool * 0.05
    }
  } else if (tipo.toUpperCase() === "G") {
    if (litros <= 20) {
      valorDesconto = litros * precoGasolina * 0.04
    } else {
      valorDesconto = litros * precoGasolina * 0.06
    }
  } else {
    return "Tipo de combustível inválido!"
  }

  valorTotal = (litros * precoGasolina) - valorDesconto

  return valorTotal
}

console.log(`O valor total a pagar é: ${Math.round(valorPagar('A', 21), 2)}`) 