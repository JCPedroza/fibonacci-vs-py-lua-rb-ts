// Check that a function evaluates to the expected output.
const assertEquals = (fun: Function, arg: number, out: number) => {
  const result = fun(arg)
  const passed = result === out

  if (!passed) {
    throw new Error(`${fun.name} failed unit test f(${arg}) === ${out} with ${result}`)
  }
}

// Run all unit test assertions for one function.
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
const testFunction = (fun: Function) => {
  console.log(`Testing algorithm ${fun.name}...`)
  assertAll(fun)
}

// Run unit tests for all functions.
export const testAllFunctions = (funs: Function[]) => {
  funs.forEach(fun => testFunction(fun))
}

export default {
  testAllFunctions
}
