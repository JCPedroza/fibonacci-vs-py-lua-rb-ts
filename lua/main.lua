package.path = package.path .. ";?.lua"
require 'test'
require 'fibo'

Test.test_all_functions(Fibos)
