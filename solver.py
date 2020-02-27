#!/usr/bin/python
import utils

def final_solver_first_degree(a,b,c,d):
	factor_up = d - b
	print ('d and b '+str(factor_up))
	factor_down = a - c
	print ('a and c '+str(factor_down))
	if factor_down < 0 and factor_up * -1 < 0:
		print ('Reduced form is : '+str(factor_down)+' * X^1 '+str(factor_up * -1)+' * X^0 = 0')
	elif factor_down < 0 and factor_up * -1 > 0:
		print ('Reduced form is : '+str(factor_down)+' * X^1 + '+str(factor_up * -1)+' * X^0 = 0')
	elif factor_down > 0 and factor_up * -1 < 0:
		print ('Reduced form is : '+str(factor_down)+' * X^1 '+str(factor_up * -1)+' * X^0 = 0')
	return factor_up/factor_down

def resolve_first_degree(left, right):
	left_no_spc = left.replace(' ', '')
	right_no_spc = right.replace(' ', '')
	print(left_no_spc, right_no_spc)
	isneg = utils.count_minus(left_no_spc, right_no_spc)
	print ('isneg = '+str(isneg))
	right_no_spc = right_no_spc.replace('-', '')
	left_no_spc = left_no_spc.replace('-', '')
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
	print ('left is :'+str(res_l), 'right is'+str(res_r))
	print (arr_left, arr_right)
	print(final_solver_first_degree(res_l[0], res_l[1], res_r[0], res_r[1]))
	return 1

def resolve_second_degree(left, right):
	return 1

def resolve_zero_degree(left, right):
	return 1
