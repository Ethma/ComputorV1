import sys
import os
import computorv1
import solver

file = 'computorv1'
test = ''

def tests():
	test_right = "5 * X^0 + 4 * X^1 - 9.3 * X^2" 
	test_left = "1 * X^0"
	solver.resolve_second_degree(test_left, test_right)
	solver.resolve_first_degree('4 * X^0', '-5 * X^0 + 4 * X^1')
	print('ENTRY = 4 * X^0', '-5 * X^0 + 4 * X^1')
	solver.resolve_first_degree('-5 * X^0 + 4 * X^1', '-5 * X^0 + 4 * X^1')
	print('ENTRY = -5 * X^0 + 4 * X^1', '-5 * X^0 + 4 * X^1')
	solver.resolve_first_degree('1 * X^0 + 4 * X^1', '-5 * X^0 + 4 * X^1')
	print('ENTRY = 1 * X^0 + 4 * X^1', '-5 * X^0 + 4 * X^1')
	solver.resolve_zero_degree('42 * X^0', '42 * X^0')
	print('ENTRY = 42 * X^0', '42 * X^0')
	solver.resolve_zero_degree('40 * X^0', '42 * X^0')
	print('ENTRY = 40 * X^0', '42 * X^0')
	solver.resolve_zero_degree(' - 42 * X^0', '42 * X^0')
	print('ENTRY =  - 42 * X^0', '42 * X^0')
	solver.resolve_zero_degree(' 42 * X^0', '0 * X^0')
	print('ENTRY =  42 * X^0', '0 * X^0')
	solver.resolve_zero_degree(' 42 * X^0', '40 * X^0')
	print('ENTRY =  42 * X^0', '40 * X^0')
	solver.resolve_zero_degree(' 42 * X^0', ' - 42 * X^0')
	print('ENTRY =  42 * X^0', ' - 42 * X^0')
tests()