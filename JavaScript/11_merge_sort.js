function merge_sort(vetor){
  if(vetor.length > 1){
    const divisao = Math.round(vetor.length/2)
    const esquerda = vetor.slice(0,divisao)
    const direita = vetor.slice(divisao,vetor.length)

    merge_sort(esquerda)
    merge_sort(direita)

    let i = 0 
    let j = 0
    let k = 0

    //ordena esquerda e direita
    while(i < esquerda.length && j < direita.length){
      if(esquerda[i] < direita[j]){
        vetor[k] = esquerda[i]
        i += 1
      } else {
        vetor[k] = direita[j]
        j += 1
      }
      k += 1
    }
    
    //ordenação final
    while(i < esquerda.length){
      vetor[k] = esquerda[i]
      i += 1
      k += 1
    }
    while(j < direita.length){
      vetor[k] = direita[j]
      j += 1
      k += 1
    }
  }

  return vetor
}


const ordenado = merge_sort([15,34,8,3])
const ordenaado_pior_caso = merge_sort([10,9,8,7,6,5,4,3,2,1])
console.log(ordenado)
console.log(ordenaado_pior_caso)
