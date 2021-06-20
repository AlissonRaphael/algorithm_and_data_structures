class Pilha {
  
  constructor(capacidade){
    this.__capacidade = capacidade
    this.__topo = -1
    this.__valores = new Array(this.__capacidade)
  }

  empilhar(valor){
    if(this.__topo === this.__capacidade - 1){
      console.log('A pilha está cheia.')
    } else {
      this.__topo += 1
      this.__valores[this.__topo] = valor
    }
  }

  desempilhar(){
    if(this.__topo === -1){
      console.log('A pilha está vazia.')
    } else {
      this.__topo -= 1
    }
  }

  buscar_topo(self){
    if(this.__topo != -1){
      return this.__valores[this.__topo]
    } else{
      return -1
    }
  }
}


const pilha = new Pilha(4)

pilha.empilhar(8)
pilha.empilhar(3)
pilha.empilhar(5)
pilha.empilhar(1)

pilha.empilhar(9)

console.log(pilha.buscar_topo())

pilha.desempilhar()
pilha.desempilhar()
pilha.empilhar(7)
console.log(pilha.buscar_topo())
