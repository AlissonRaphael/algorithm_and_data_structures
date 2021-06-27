function insertion_sort(vetor){
  const n = vetor.length

  for(let i = 1; i < n; i++){
    let selecionado = vetor[i]

    let j = i - 1
    while(j >= 0 && selecionado < vetor[j]){
      vetor[j+1] = vetor[j]
      j -= 1
    }
    vetor[j+1] = selecionado
  }

  return vetor
}


const ordenado = insertion_sort([15,34,8,3])
const ordenaado_pior_caso = insertion_sort([10,9,8,7,6,5,4,3,2,1])
console.log(ordenado)
console.log(ordenaado_pior_caso)
