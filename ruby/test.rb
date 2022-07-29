def assert_equals(fun, arg, out)
  result = fun.call(arg)
  passed = result == out

  if !passed
    raise "#{fun.name} failed unit test f(#{arg}) == #{out} with #{result}"
  end
end
