function selection_sort(vetor){
  const n = vetor.length

  for(let i = 0; i < n; i++){
    let index_min = i

    for(let j = i+1; j < n; j++){
      if(vetor[index_min] > vetor[j]) index_min = j
    }

    let temp = vetor[i]
    vetor[i] = vetor[index_min]
    vetor[index_min] = temp
  }

  return vetor
}

const ordenado = selection_sort([15,34,8,3])
const ordenado_pior_caso = selection_sort([10,9,8,7,6,5,4,3,2,1])

console.table(ordenado)
console.table(ordenado_pior_caso)
