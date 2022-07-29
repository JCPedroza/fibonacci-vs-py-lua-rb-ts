-- Compute nth Fibonacci number using simple recursion with if statement.
local function fibo_simple(index)
  if index < 2 then
    return index
  end

  return fibo_simple(index - 1) + fibo_simple(index - 2)
end

-- Compute nth Fibonacci number using tail call.
local function fibo_tail_call(index)
  local function loop(now, next, index)
    if index == 0 then
      return now
    end

    return loop(next, now + next, index - 1)
  end

  return loop(0, 1, index)
end

-- Compute nth Fibonacci number using memoization.
local function fibo_memoized(index)
  local results = {[0] = 0, [1] = 1}

  local function loop(index)
    if results[index] ~= nil then
      return results[index]
    end

    results[index] = loop(index - 1) + loop(index - 2)
    return results[index]
  end

  return loop(index)
end

-- Compute nth Fibonacci number using a for loop.
local function fibo_for_loop(index)
  local now, nxt = 0, 1

  for loop = 1, index do
    now, nxt = nxt, now + nxt
  end

  return now
end

-- Compute nth Fibonacci number using Binet's formula.
local function fibo_binet(index)
  if index == 0 then -- Otherwise f(0) = 1
    return 0
  end

  local sqrt5 = math.sqrt(5)
  p = (1 + sqrt5) / 2
  q = 1 / p

  return math.floor((p^index + q^index) / sqrt5 + 0.5)
end

Fibos = {
  {fibo_simple, 'fibo_simple'},
  {fibo_tail_call, 'fibo_tail_call'},
  {fibo_memoized, 'fibo_memoized'},
  {fibo_for_loop, 'fibo_for_loop'},
  {fibo_binet, 'fibo_binet'}
}

return Fibos
