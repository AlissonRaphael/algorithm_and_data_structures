function particao(vetor, inicio, final){
  const pivo = vetor[final]
  let i = inicio - 1

  for(let j = inicio; j < final; j++){
    if(vetor[j] <= pivo){
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
    }
  }

  vetor[i+1], vetor[final] = vetor[final], vetor[i+1]

  return i+1
}

function quick_sort(vetor, inicio, final){
  if(inicio < final){
    const posicao = particao(vetor, inicio, final)
    quick_sort(vetor, inicio, posicao-1) // esquerda
    quick_sort(vetor, posicao+1, final) // direita
  }

  return vetor
}

const desordenado = [15,34,8,3]
const ordenado = quick_sort(desordenado, 0, desordenado.length-1)
console.log(ordenado)

const desordenado_pior_caso = np.array([10,9,8,7,6,5,4,3,2,1])
const ordenaado_pior_caso = quick_sort(desordenado_pior_caso, 0, len(desordenado_pior_caso)-1)
console.log(ordenaado_pior_caso)
