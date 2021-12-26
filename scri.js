
class Sqrt {

      constructor(x){
  
        this.raiz = x

      }

      calc(){

        return  Math.sqrt(this.raiz)
      }
}


sqrt = new Sqrt(36)
console.log(sqrt.calc())