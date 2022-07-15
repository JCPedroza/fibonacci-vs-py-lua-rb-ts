/**
 * Run me with: deno run fibo.ts
 */

/**
 * Compute nth Fibonacci number using simple recursion.
 */
function fibo_simple (index: number): number {
  if (index < 2) return index
  return fibo_simple(index - 1) + fibo_simple(index - 2)
}

console.log(fibo_simple(6))
