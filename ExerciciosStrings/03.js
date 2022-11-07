// Faça um programa que solicite o nome do usuário e imprima­o na vertical

function imprimirNomeVertical(nome) {
  for (let i = 0; i < nome.length; i++) {
    console.log(nome[i] + '\n')
  }
}

imprimirNomeVertical('joao')