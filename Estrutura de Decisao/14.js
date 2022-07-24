/*
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média.
*/

const mediaa = (num1, num2) => num1 + num2

const mediaConceito = (num1, num2) => {
  let media = mediaa(num1, num2)
  
  let conceito
  let aprovacao

  if (media >= 0 && media < 4) {
    conceito = 'E'
    aprovacao = 'REPROVADO'
  } else if (media >= 4 && media < 6) {
    conceito = 'D'
    aprovacao = 'REPROVADO'
  } else if (media >= 6 && media < 7.5) {
    conceito = 'C'
    aprovacao = 'APROVADO'
  } else if (media >= 7.5 && media < 9) {
    conceito = 'B'
    aprovacao = 'APROVADO'
  } else if (media >= 9 && media <= 10) {
    conceito = 'A'
    aprovacao = 'APROVADO'
  } else {
    return 'Media Inválida'
  }

  return {conceito, aprovacao }
}

console.log(mediaConceito(1,3))