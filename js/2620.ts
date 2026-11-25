function createCounter(n: number): () => number {
    return function() {
        return n++;
        
    }
}


const counter = createCounter(10)
console.log(counter())
console.log(counter())
console.log(counter())
/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */