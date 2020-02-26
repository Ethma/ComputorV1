#!/usr/bin/python

import sys
import solver
import utils
def	parse():
	operation = sys.argv[1].split("=")
	left = operation[0]
	right = operation[1]
	degree = -1
	left_degree = utils.get_degree(left)
	right_degree = utils.get_degree(right)
	if left_degree > right_degree:
		degree = left_degree
	else:
		degree = right_degree
	if degree == -1:
		return print('Syntax error, there is no ^X in your entree, please double check it.')
	print('Polynomial degree : '+str(degree))
	if degree == 0:
		res = solver.resolve_zero_degree(left, right)
	elif degree == 1:
		res = solver.resolve_first_degree(left, right)
	elif degree == 2:
		res = solver.resolve_second_degree(left, right)
	elif degree > 2:
		res = -1
		print('The Polynomial degree is stricly greater than 2. I can\'t solve.')
	return res
def main():
	if len(sys.argv) == 2:
		parse()
main()