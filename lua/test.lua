local test = {}

-- Check that a function evaluates to the expected output
function test.assert_equals(fun, arg, out)
  local result = fun[1](arg)
  local passed = result == out

  assert(
    passed,
    string.format(
      '%s failed unit test f(%d) == %d with %d',
      fun[2],
      arg,
      out,
      result)
  )
end

-- Run all unit tests assertions for one function.
function test.assert_all(fun)
  test.assert_equals(fun, 0, 0)
  test.assert_equals(fun, 1, 1)
  test.assert_equals(fun, 2, 1)
  test.assert_equals(fun, 3, 2)
  test.assert_equals(fun, 4, 3)
  test.assert_equals(fun, 5, 5)
  test.assert_equals(fun, 6, 8)
  test.assert_equals(fun, 30, 832040)
end

-- Perorm unit tests for one algorithm.
function test.test_function(fun)
  print(string.format('Testing algorithm %s...', fun[2]))
  test.assert_all(fun)
end

-- Run unit tests for all functions.
function test.test_all_functions(funs)
  for _, fun in ipairs(funs) do
    test.test_function(fun)
  end
end

return test
