import sys
import os
import computorv1
import solver

file = 'computorv1'
test = ''

def tests():
	test = '\"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"'
	cmd = 'python3 computorv1.py {}'.format(test)
	print (cmd)
	os.system(cmd)
	test = '\"5 * X^0 + 4 * X^1 = 4 * X^0\"'
	print (cmd)
	os.system(cmd)

tests()