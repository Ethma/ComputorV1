#!/usr/bin/python
import utils

def final_solver_first_degree(a,b,c,d, isneg):
	factor_up = d - b
	factor_down = a - c
	print ('a and c = '+str(factor_down))
	print ('d and b = '+str(factor_up))
	if factor_down < 0 and factor_up * -1 < 0:
		print ('Reduced form is : '+str(factor_down)+' * X^1 '+str(factor_up * -1)+' * X^0 = 0')
	elif factor_down < 0 and factor_up * -1 > 0:
		print ('Reduced form is : '+str(factor_down)+' * X^1 + '+str(factor_up * -1)+' * X^0 = 0')
	elif factor_down > 0 and factor_up * -1 < 0:
		print ('Reduced form is : '+str(factor_down)+' * X^1 '+str(factor_up * -1)+' * X^0 = 0')
	else:
		print ('Reduced form is : '+str(factor_down)+' * X^1 - '+str(factor_up * -1)+' * X^0 = 0')
	if isneg == 1:
		return float(factor_up) / float(factor_down)
	return float(factor_up)/float(factor_down) * -1
""" 
def resolve_first_degree(left, right):
	left_no_spc = left.replace(' ', '')
	right_no_spc = right.replace(' ', '')
	isneg, left_no_spc, right_no_spc = utils.count_minus(left_no_spc, right_no_spc)
	print ('isneg = '+str(isneg))
	arr_left = left_no_spc.split('+')
	arr_right = right_no_spc.split('+')
	res_l = []
	res_r = []
	tmp_arr_left, tmp_arr_left2 = utils.extract_numbers(arr_left)
	tmp_arr_right, tmp_arr_right2 = utils.extract_numbers(arr_right)
	res_l.append(utils.sum_of_num(tmp_arr_left))
	res_l.append(utils.sum_of_num(tmp_arr_left2))
	res_r.append(utils.sum_of_num(tmp_arr_right))
	res_r.append(utils.sum_of_num(tmp_arr_right2))
	print ('left is : '+str(res_l), 'right is : '+str(res_r))
	print(final_solver_first_degree(res_l[0], res_l[1], res_r[0], res_r[1], isneg))
	return 1
 """

def resolve_first_degree(left, right):
	left_numbers, left_x = utils.extract_numbers(left)
	left_numbers = utils.clean_list(left_numbers, 'left')
	left_x = utils.clean_vars(left_x, 'left')
	right_numbers, right_x = utils.extract_numbers(right)
	right_numbers = utils.clean_list(right_numbers, 'right')
	right_x = utils.clean_vars(right_x, 'right')
	left_numbers = left_numbers + right_numbers
	print(left_x, right_x)
	unkowns_cleaned = dict(list(left_x.items()) + list(right_x.items()))
	print(unkowns_cleaned)
	return 1
def resolve_second_degree(left, right):
	return 1

def resolve_zero_degree(left, right):
	return 1
