#!/usr/bin/python
import utils

def final_solver_first_degree(a,b,c,d):
	factor_up = d - b
	factor_down = a - c
	print ('a and c = '+str(factor_down))
	print ('d and b = '+str(factor_up))
	return float(factor_up)/float(factor_down) * -1

def resolve_first_degree(left, right):
	left_numbers, left_x = utils.extract_numbers(left)
	left_numbers = utils.clean_list(left_numbers, 'left')
	left_x = utils.clean_vars(left_x, 'left')
	right_numbers, right_x = utils.extract_numbers(right)
	right_numbers = utils.clean_list(right_numbers, 'right')
	right_x = utils.clean_vars(right_x, 'right')
	numbers_cleaned = left_numbers + right_numbers
	unkowns_cleaned, numbers_cleaned = utils.final_clean(left_x, right_x, numbers_cleaned)
	if numbers_cleaned > 0:
		print ('Reduced form is : '+str(unkowns_cleaned[1])+' * X^1 + '+str(numbers_cleaned)+' * X^0 = 0')
	else:
		print ('Reduced form is : '+str(unkowns_cleaned[1])+' * X^1 - '+str(numbers_cleaned * -1)+' * X^0 = 0')
	print (numbers_cleaned / unkowns_cleaned[1])
	return 1
def resolve_second_degree(left, right):
	return 1

def resolve_zero_degree(left, right):
	return 1
