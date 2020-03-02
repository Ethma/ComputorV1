#!/usr/bin/python
import utils

def final_solver_first_degree(factor_up, factor_down):
	utils.get_reduced_form(factor_up, factor_down[1], None, 1)
	if factor_up == 0 and factor_down[1] == 0:
		print('The solution is :')
		print ('all the real numbers')
		return 1
	elif factor_down[1] == 0 and factor_up != 0:
		print ('There are no value of X that make equation true.')
		print ('There is no solution')
		return 1
	print('The solution is :')
	if float(factor_up)/float(factor_down[1]) != 0: 
		print (float(factor_up)/float(factor_down[1]) * -1)
	else:
		print (float(factor_up)/float(factor_down[1]))

def final_solver_second_degree(a, b, c):
	discriminant = utils.get_discriminant(a, b, c)
	utils.get_results(a, b, discriminant)

def resolve_first_degree(left, right):
	left_numbers, left_x = utils.extract_numbers(left, 1)
	left_numbers = utils.clean_list(left_numbers, 'left')
	left_x = utils.clean_vars(left_x, 'left')
	right_numbers, right_x = utils.extract_numbers(right, 1)
	right_numbers = utils.clean_list(right_numbers, 'right')
	right_x = utils.clean_vars(right_x, 'right')
	unkowns_cleaned, numbers_cleaned = utils.final_clean(left_x, right_x, left_numbers + right_numbers, 1)
	final_solver_first_degree(numbers_cleaned, unkowns_cleaned)

def resolve_zero_degree(left, right):
	left_numbers = utils.extract_numbers(left, 0)
	left_numbers = utils.clean_list(left_numbers, 'left')
	right_numbers = utils.extract_numbers(right, 0)
	right_numbers = utils.clean_list(right_numbers, 'right')
	left_numbers = utils.final_clean({}, {}, left_numbers, 0)
	right_numbers = utils.final_clean({}, {}, right_numbers, 0)
	right_numbers *= -1
	utils.get_reduced_form(None, left_numbers, right_numbers, 0)

def resolve_second_degree(left, right):
	left_numbers, left_x = utils.extract_numbers(left, 2)
	left_numbers = utils.clean_list(left_numbers, 'left')
	left_x = utils.clean_vars(left_x, 'left')
	right_numbers, right_x = utils.extract_numbers(right, 2)
	right_numbers = utils.clean_list(right_numbers, 'right')
	right_x = utils.clean_vars(right_x, 'right')
	unkown_cleaned, numbers_cleaned = utils.final_clean(left_x, right_x, right_numbers + left_numbers, 1)
	final_solver_second_degree(unkown_cleaned[2], unkown_cleaned[1], numbers_cleaned, discriminant)
	return 1
