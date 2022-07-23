# Compute nth Fibonacci number using simple recursion.
def fibo_simple(index)
  return index if index < 2

  fibo_simple(index - 1) + fibo_simple(index - 2)
end

# Compute nth Fibonacci number using tail call.
def fibo_tail_call(index)
  def iter(now, nxt, index)
    return now if index == 0

    iter(nxt, now + nxt, index - 1)
  end

  iter(0, 1, index)
end

fibs_to_test = [
  method(:fibo_simple),
  method(:fibo_tail_call)
]

fibs_to_test.each { |fibo| puts(fibo.call(6)) }
