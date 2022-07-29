# Check that function applied to argument evaluates to the expected output.
def assert_equals(fun, arg, out)
  result = fun.call(arg)
  passed = result == out

  if !passed
    raise "#{fun.name} failed unit test f(#{arg}) == #{out} with #{result}"
  end
end

# Run all unit test assertions for one function.
def assert_all(fun)
  assert_equals(fun, 0, 0)
  assert_equals(fun, 1, 1)
  assert_equals(fun, 2, 1)
  assert_equals(fun, 3, 2)
  assert_equals(fun, 4, 3)
  assert_equals(fun, 5, 5)
  assert_equals(fun, 6, 8)
  assert_equals(fun, 30, 832_040)
end

# Perform unit tests for one function.
def test_function(fun)
  puts("Testing algorithm #{fun.name}...")
  assert_all(fun)
end

# Run unit tests for all functions.
def test_all_functions(funs)
  funs.each { |fun| test_function(fun)}
end
