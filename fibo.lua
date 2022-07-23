-- Compute nth Fibonacci number using simple recursion.
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

local fibos_to_test = {
  fibo_simple,
  fibo_tail_call
}

for _, fibo in ipairs(fibos_to_test) do
  print(fibo(6))
end
