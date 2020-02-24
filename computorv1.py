#!/usr/bin/python

import sys
from solver import *

def	parse():
	operation = sys.argv[1].split("=")
	left = operation[0].replace(' ', '')
	right = operation[1].replace(' ', '')
	degree = 0
	if left.find('X^') != -1:
		index = left.find('X^')
		i = index + 2
		while i < len(left) and left[i] != ' ':
			i += 1
			print (left[i])
		degree = int(left[index + 2: i])
		print (degree)
	if right.find('X^') != -1:
		index = right.find('X^')
		i = index + 2
		while i < len(right) and right[i] != ' ':
			i += 1
		tmp_degree = int(right[index + 2: i])
		if tmp_degree > degree:
			degree = tmp_degree
	print('Polynomial degree : '+str(degree))
	if degree == 0:
		res = resolve_zero_degree(left, right)
	elif degree == 1:
		res = resolve_first_degree(left, right)
	elif degree == 2:
		res = resolve_second_degree(left, right)
	elif degree > 2:
		print('The Polynomial degree is stricly greater than 2. I can\'t solve.')
def main():
	if len(sys.argv) == 2:
		parse()

main()