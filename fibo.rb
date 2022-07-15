# frozen_string_literal: true

# Run me with ruby fibo.rb

# Compute nth Fibonacci number using simple recursion.
def fibo_simple(index)
  return index if index < 2

  fibo_simple(index - 1) + fibo_simple(index - 2)
end

# Compute nth Fibonacci number using a times loop.
def fibo_times(index)
  now = 0
  nxt = 1

  index.times do |_|
    now, nxt = nxt, now + nxt
  end

  now
end

puts fibo_simple 6
puts fibo_times 6
