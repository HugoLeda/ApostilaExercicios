function twoNumbersInt() {
  let n1 = Number(prompt('Infomr o primeiro número: '));
  let n2 = Number(prompt('Infomr o segundo número: '));
  alert(`O produto do dobro do primeiro: ${(n1 * 2) * (n1 * 2)} com metade do segundo: ${n2 / 2} = ${((n1 * 2) * (n1 * 2)) + (n2 / 2)} `);
}

function heightPeople() {
  /* 
  Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) ­- 58
  */
  let altura = Number(prompt('Infomr o sua altura(x.xx(m)): '));
  const pesoIdeal = (72.7*altura) - 58
  alert(`O seu peso ideal é ${pesoIdeal}`)
}