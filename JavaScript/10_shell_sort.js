function shell_sort(vetor){
  let intervalo = vetor.length

  while(intervalo > 0){
    for(let i = intervalo; i < vetor.length; i++){
      let temp = vetor[i]
      let j = i

      while(j >= intervalo && vetor[j-intervalo] > temp){
        vetor[j] = vetor[j-intervalo]
        j -= intervalo
      }

      vetor[j] = temp
    }

    intervalo = Math.floor(intervalo/2)

  }

  return vetor
}

const ordenado = shell_sort([15,34,8,3])
const ordenaado_pior_caso = shell_sort([10,9,8,7,6,5,4,3,2,1])
console.log(ordenado)
console.log(ordenaado_pior_caso)
