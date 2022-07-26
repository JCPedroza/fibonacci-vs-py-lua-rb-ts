/**
 * Number.MAX_SAFE_ITEGER is     9_007_199_254_740_991
 * The 78th Fibonacci number is  8_944_394_323_791_464
 * The 79th Fibonacci number is 14_472_334_024_676_221
 *
 * This program doesn't use BigInt, so the limit for the index of these algorithms is
 * f(78) at best, perhaps lower for some closed-form solutions that lose accuracy at
 * large values.
 */

import { testAllFunctions } from './test'


// Compute nth Fibonacci number using simple recursion.
function fiboSimpleIf(index: number): number {
  if (index < 2) return index

  return fiboSimpleIf(index - 1) + fiboSimpleIf(index - 2)
}

// Compute nth Fibonacci number using simple recursion and a switch.
function fiboSimpleSwitch(index: number): number {
  switch (index < 2) {
    case true:
      return index
    default:
      return fiboSimpleSwitch(index - 1) + fiboSimpleSwitch(index - 2)
  }
}

// Compute nth Fibonacci number using tail call.
function fiboTailCall(index: number ): number {
  function loop(now: number, next: number, index: number): number {
    if (index === 0) return now

    return loop(next, now + next, index - 1)
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

// Compute nth Fibonacci number using a for loop.
function fiboForLoop(index: number): number {
  let now = 0
  let next = 1

  for (let loop = 0; loop < index; loop++) {
    [now, next] = [next, now + next]
  }

  return now
}

// Compute nth Fibonacci number using a while loop.
function fiboWhileLoop(index: number): number {
  let now = 0
  let next = 1
  let loop = 0

  while (loop < index) {
    [now, next] = [next, now + next]
    loop++
  }

  return now
}

// Compute nth Fibonacci number using a generator function.
function fiboGenerator(index: number): number {
  function * genloop() {
    let now = 0
    let next = 1

    while (true) {
      yield now
      ;[now, next] = [next, now + next]
    }
  }

  const gen = genloop()
  for (let count = 0; count < index; count++) {
    gen.next()
  }

  return gen.next().value!
}

// Compute nth Fibonacci number using Binet's formula.
function fiboBinet(index: number): number {
  if (index === 0) return 0 // Otherwise f(0) = 1

  const sqrt5 = Math.sqrt(5)
  const p = (1 + sqrt5) / 2
  const q = 1 / p

  return Math.trunc((p**index + q**index) / sqrt5 + 0.5)
}


// Algorithms to unit test and profile.
const fibosToTest: Function[] = [
  fiboSimpleIf,
  fiboSimpleSwitch,
  fiboTailCall,
  fiboMemoizedArray,
  fiboMemoizedObject,
  fiboMemoizedMap,
  fiboForLoop,
  fiboWhileLoop,
  fiboBinet,
  fiboGenerator
]

testAllFunctions(fibosToTest)
