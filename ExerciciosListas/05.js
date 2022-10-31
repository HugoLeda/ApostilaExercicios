/*Faça um Programa que leia 20 números inteiros e armazene­os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores.*/

function ran(tamanho) {
  let numeros = [];

  for (let i = 0; i < tamanho; i++ ) {
    numeros.push(Math.round(Math.random() * 100))
  }

  return numeros;
}

function imparesPares(vetor) {
  let impares = []
  let pares = []

  for (let i = 0; i < vetor.length; i++) {
    if (vetor[i] % 2 == 0) {
      pares.push(vetor[i])
    } else {
      impares.push(vetor[i])
    }
  }

  return ({
    vetor,
    pares,
    impares
  })
}

console.log(imparesPares(ran(10)))