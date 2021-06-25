function bubble_sort(vetor){
  const n = vetor.length

  for(let i = 0; i < n; i++){
    let m = n - i - 1
    for(let j = 0; j < m; j++){
      if(vetor[j] > vetor[j+1]){
        const temp = vetor[j]
        vetor[j] = vetor[j+1]
        vetor[j+1] = temp
      }
    }

  }
  return vetor
}

const ordenado = bubble_sort([15,34,8,3])
const ordenado_pior_caso = bubble_sort([10,9,8,7,6,5,4,3,2,1])

console.table(ordenado)
console.table(ordenado_pior_caso)
