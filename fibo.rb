# Run me with ruby fibo.rb

# Compute nth Fibonacci number using simple recursion.
def fibo_simple index
  return index if index < 2
  return fibo_simple(index - 1) + fibo_simple(index - 2)
end

puts fibo_simple 6
