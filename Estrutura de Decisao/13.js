/*
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1­Domingo, 2­ Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
*/

const diaSemana = (codigo) => {
  let resultado
  switch (codigo) {
    case 1:
      resultado = 'Domingo'
      break;
    case 2:
      resultado = 'Segunda-feira'
      break;
    case 3:
      resultado = 'Terça-feira'
      break;
    case 4:
      resultado = 'Quarta-feira'
      break;
    case 1:
      resultado = 'Quinta-feira'
      break;
    case 1:
      resultado = 'Sexta-feira'
      break;      
    case 1:
      resultado = 'Sábado'
      break;
    default:
      resultado = 'Valor inválido'
      break;    
  }

  return resultado
}

console.log(diaSemana(1))