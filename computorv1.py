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
	if left_degree == -2:
		print('Syntax error, something goes wrong with your entree, please double check it.')
		return -1
	right_degree = utils.get_degree(right)
	if left_degree > right_degree:
		degree = left_degree
	else:
		degree = right_degree
	if degree <= -1:
		print('Syntax error, something goes wrong with your entree, please double check it.')
		return -1
	if degree == 0:
		solver.resolve_zero_degree(left, right)
	elif degree == 1:
		solver.resolve_first_degree(left, right)
	elif degree == 2:
		solver.resolve_second_degree(left, right)
	elif degree > 2:
		print('The Polynomial degree is stricly greater than 2. I can\'t solve.')
def main():
	if len(sys.argv) == 2:
		parse()
main()