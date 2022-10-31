/*
aça um programa que receba a temperatura média de cada mês do ano e armazene­as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
*/

const temperaturas = [
  ["janeiro", 25],
  ["fevereiro", 22],
  ["março", 26],
  ["abril", 22],
  ["maio", 24],
  ["juhno", 21],
  ["julho", 19],
  ["agosto", 18],
  ["setembro", 20],
  ["outubro", 24],
  ["novembro", 25],
  ["dezembro", 27]
]

function mediaAnual(temperaturas) {
  let soma = 0

  for (let i = 0; i < temperaturas.length; i++) {
    soma += temperaturas[i][1]
  }

  let media = soma / temperaturas.length
  
  return media
}

function main(temperaturas) {
  let acimaMedia = []
  let abaixoMedia = []

  const media = mediaAnual(temperaturas)

  for (let i = 0; i < temperaturas.length; i++) {
    if (temperaturas[i][1] >= media) {
      acimaMedia.push(temperaturas[i])
    } else {
      abaixoMedia.push(temperaturas[i])
    }
  }

  console.log(`Média anual: ${media}`)

  console.log("Meses acima da média:\n")
  for (let i = 0; i < acimaMedia.length; i++) {
    console.log(acimaMedia[i])
  }

  console.log("\nMeses abaixo da média: \n")
  for (let i = 0; i < abaixoMedia.length; i++) {
    console.log(abaixoMedia[i])
  }
}

main(temperaturas)