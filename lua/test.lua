Test = {}

-- Check that a function evaluates to the expected output
local function assert_equals(fun, arg, out)
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
local function assert_all(fun)
  assert_equals(fun, 0, 0)
  assert_equals(fun, 1, 1)
  assert_equals(fun, 2, 1)
  assert_equals(fun, 3, 2)
  assert_equals(fun, 4, 3)
  assert_equals(fun, 5, 5)
  assert_equals(fun, 6, 8)
  assert_equals(fun, 30, 832040)
end

-- Perform unit tests for one algorithm.
local function test_function(fun)
  print(string.format('Testing algorithm %s...', fun[2]))
  assert_all(fun)
end

-- Run unit tests for all functions.
function Test.test_all_functions(funs)
  for _, fun in ipairs(funs) do
    test_function(fun)
  end
end

return Test
