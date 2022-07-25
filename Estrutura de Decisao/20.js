/*
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e presentar:
a.  A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b.  A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c.  A mensagem "Aprovado com Distinção", se a média for igual a 10
*/

const media = (notas) => {
  let soma = 0

  for (let i = 0; i < notas.length; i++) {
    if (notas[i] < 0 || notas[i] > 10) {
      return 'Notas invalidas'
    }
    soma += notas[i]
  }

  soma = soma / notas.length

  return soma
}

const aprovacao = (nota1,nota2, nota3) => {
  const mediaAluno = media([nota1, nota2, nota3])
  if (mediaAluno == 'Notas invalidas') {
    return mediaAluno
  }

  let mensagem
  if (mediaAluno < 7) {
    mensagem = 'Reprovado'
  } else if (mediaAluno >= 7 && mediaAluno < 10) {
    mensagem = 'Aprovado'
  } else if (mediaAluno == 10) {
    mensagem = 'Aprovado com Distinção'
  } else {
    throw new Error('media invalida') 
  }

  return {mensagem, mediaAluno}
}

console.log(aprovacao(10,7,8))