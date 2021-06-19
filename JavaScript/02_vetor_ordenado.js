class VetorOrdenado {

  constructor(capacidade){
    this.capacidade = capacidade
    this.ultima_posicao = -1
    this.valores = new Array(this.capacidade)
  }

  imprime(){
    if(this.ultima_posicao === -1){
      console.log('O vetor está vazio.')
    } else {
      for(let i = 0; i <= this.ultima_posicao; i++){
        console.log(`Index ${i}: ${this.valores[i]}`)
      }
    }
  }

  insere(valor){
    if(this.ultima_posicao === this.capacidade - 1){ 
      console.log('Capacidade máxima atingida.')
      return
    }

    let posicao = 0
    for(let i = 0; i <= this.ultima_posicao; i++){
      posicao = i
      if(this.valores[i] > valor){
        break
      } else if(i === this.ultima_posicao){
        posicao = i + 1
      }
    }

    let x = this.ultima_posicao
    while(x >= posicao){
      this.valores[x+1] = this.valores[x]
      x -= 1
    }

    this.valores[posicao] = valor
    this.ultima_posicao += 1

  }

  pesquisar(valor){
    for(let i = 0; i <= this.ultima_posicao; i++){
      if(this.valores[i] > valor) return -1
      if(this.valores[i] === valor) return i
      if(i === this.ultima_posicao) return -1
    }

    return -1
  }

  excluir(valor){
    const posicao = this.pesquisar(valor)
    if(posicao === -1){
      return -1
    } else {
      for(let i = posicao; i < this.ultima_posicao; i++){
        this.valores[i] = this.valores[i+1]
      }
      this.ultima_posicao -= 1
    }
  }
}


const vetor = new VetorOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(8)
vetor.insere(9)
vetor.insere(1)
vetor.imprime()

vetor.insere(4)
console.log(vetor.pesquisar(9))
console.log(vetor.pesquisar(11)) //pior caso: não existe no vetor.
console.log(vetor.pesquisar(2)) //melhor caso: na primeira posição.

vetor.imprime()
vetor.excluir(3)
vetor.imprime()