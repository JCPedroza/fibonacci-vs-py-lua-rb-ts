require_relative "./test.rb"

# Compute nth Fibonacci number using simple recursion and an if statement.
def fibo_simple_if(index)
  return index if index < 2

  fibo_simple_if(index - 1) + fibo_simple_if(index - 2)
end

# Compute nth Fibonacci number using simple recursion and a case expression.
def fibo_simple_case(index)
  case index < 2
  when true
    index
  else
    fibo_simple_case(index - 1) + fibo_simple_case(index - 2)
  end
end

# Compute nth Fibonacci number using tail call.
def fibo_tail_call(index)
  def iter(now, nxt, index)
    return now if index == 0

    iter(nxt, now + nxt, index - 1)
  end

  iter(0, 1, index)
end

# Compute nth Fibonacci number using the times method.
def fibo_times_loop(index)
  now, nxt = 0, 1

  index.times do
    now, nxt = nxt, now + nxt
  end

  now
end

# Compute nth Fibonacci number using Binet's formula
def fibo_binet(index)
  return 0 if index == 0 # Otherwise f(0) = 1

  sqrt5 = Math.sqrt(5)
  p = (1 + sqrt5) / 2
  q = 1 / p

  ((p**index + q**index) / sqrt5 + 0.5).to_i
end

fibs_to_test = [
  method(:fibo_simple_if),
  method(:fibo_simple_case),
  method(:fibo_tail_call),
  method(:fibo_times_loop),
  method(:fibo_binet)
]

fibs_to_test.each { |fibo| puts(fibo.call(6)) }
