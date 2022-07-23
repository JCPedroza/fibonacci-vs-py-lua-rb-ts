// Compute nth Fibonacci number using simple recursion.
function fiboSimple(index: number): number {
  if (index < 2) return index

  return fiboSimple(index - 1) + fiboSimple(index - 2)
}

// Compute nth Fibonacci number using tail call.
function fiboTailCall(index: number ): number {
  function loop(now: number, nxt: number, index: number): number {
    if (index === 0) return now

    return loop(nxt, now + nxt, index - 1)
  }

  return loop(0, 1, index)
}

// Compute nth Fibonacci number using memoization with array.
function fiboMemoizedArray(index: number): number {
  const results: number[] = [0, 1]

  function loop(index: number): number {
    if (results[index] !== undefined) return results[index]

    results[index] = loop(index - 1) + loop(index - 2)
    return results[index]
  }

  return loop(index)
}

// Compute nth Fibonacci number using memoization with object literal.
function fiboMemoizedObject(index: number): number {
  const results: {[key: number]: number} = {0: 0, 1: 1}

  function loop(index: number): number {
    if (index in results) return results[index]

    results[index] = loop(index - 1) + loop(index - 2)
    return results[index]
  }

  return loop(index)
}

// Compute nth Fibonacci number using memoization with map.
function fiboMemoizedMap(index: number): number {
  const results: Map<number, number> = new Map()
  results.set(0, 0)
  results.set(1, 1)

  function loop(index: number): number {
    if (results.has(index)) return results.get(index)!

    results.set(index, loop(index - 1) + loop(index - 2))
    return results.get(index)! // ! is non-null assertion for type check
  }

  return loop(index)
}

const fibosToTest: Function[] = [
  fiboSimple,
  fiboTailCall,
  fiboMemoizedArray,
  fiboMemoizedObject,
  fiboMemoizedMap
]

fibosToTest.forEach(fibo => console.log(`${fibo.name}: ${fibo(6)}`))
