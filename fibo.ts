// Compute nth Fibonacci number using simple recursion.
function fiboSimple(index: number): number {
  if (index < 2) return index

  return fiboSimple(index - 1) + fiboSimple(index - 2)
}

// Compute nth Fibonacci number using simpre recursion and a switch.
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

// Algorithms to unit test and profile.
const fibosToTest: Function[] = [
  fiboSimple,
  fiboSimpleSwitch,
  fiboTailCall,
  fiboMemoizedArray,
  fiboMemoizedObject,
  fiboMemoizedMap,
  fiboForLoop,
  fiboWhileLoop
]

// Testing

// Check that a function evaluates to the expected output.
const assertEquals = (fun: Function, arg: number, out: number) => {
  const result = fun(arg)
  const passed = result === out

  if (!passed) {
    throw new Error(`${fun.name} failed unit test f(${arg}) === ${out} with ${result}`)
  }
}

// Run all unit test assertions.
const assertAll = (fun: Function) => {
  assertEquals(fun, 0, 0)
  assertEquals(fun, 1, 1)
  assertEquals(fun, 2, 1)
  assertEquals(fun, 3, 2)
  assertEquals(fun, 4, 3)
  assertEquals(fun, 5, 5)
  assertEquals(fun, 6, 8)
  assertEquals(fun, 30, 832_040)
}

// Perform unit tests for one algorithm.
const testFunction = (fun: Function, verbose: boolean = true) => {
  if (verbose) {
    console.log(`Testing algorithm ${fun.name}...`)
  }

  assertAll(fun)
}

// Run unit tests for all functions.
const testAllFunctions = (funs: Function[]) => {
  funs.forEach(fun => testFunction(fun))
}

testAllFunctions(fibosToTest)
