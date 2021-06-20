class FilaCircular{

  constructor(capacidade){
    this.__capacidade = capacidade
    this.inicio = 0
    this.final = -1
    this.numero_elementos = 0
    this.valores = new Array(this.__capacidade)
  }

  enfileirar(valor){
    if(this.numero_elementos === this.__capacidade){
      console.log('A fila está cheia.')
      return
    }

    if(this.final === this.__capacidade - 1){
      this.final = -1
    }

    this.final += 1
    this.valores[this.final] = valor
    this.numero_elementos += 1
  }

  desenfileirar(){
    if(this.numero_elementos === 0){
      console.log('A fila está vazia.')
      return
    }

    const temp = this.valores[this.inicio]
    this.inicio += 1

    if(this.inicio === this.__capacidade - 1){
      this.inicio = 0
    }

    this.numero_elementos -= 1
    return temp
  }

  primeiro(){
    if(this.numero_elementos === 0) return -1

    return this.valores[this.inicio]
  }
}


const fila = new FilaCircular(5)

fila.enfileirar(7)
fila.enfileirar(4)
fila.enfileirar(1)
fila.enfileirar(8)
fila.enfileirar(3)
console.log(`\x1b[31m${fila.valores}\x1b[0m`)

console.log(fila.primeiro())
console.log(fila.desenfileirar())
console.log(fila.desenfileirar())
console.log(`\x1b[31m${fila.valores}\x1b[0m`)


fila.enfileirar(6)
fila.enfileirar(7)
console.log(`\x1b[31m${fila.valores}\x1b[0m`)


console.log(fila.primeiro())
