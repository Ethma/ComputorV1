import sys
import os
import computorv1
import solver

file = 'computorv1'
test = ''

def which_one(number):
	if number == "1":
		tests_basics()
	if number == "2":
		tests_intermediate()
	return 1

def tests_intermediate():
	pass

def tests_basics():
	test_right = "5 * X^0 + 4 * X^1 - 9.3 * X^2" 
	test_left = "1 * X^0"
	solver.resolve_second_degree(test_left, test_right)
	test_left = '4 * X^0'
	test_right = '-5 * X^0 + 4 * X^1'
	solver.resolve_first_degree(test_left, test_right)
if len(sys.argv) == 2:
	which_one(sys.argv[1])