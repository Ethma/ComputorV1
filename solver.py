#!/usr/bin/python

def final_solver(a,b,c,d):
	return (d - b)/(a - c)

def sum_of_num(numb_array):
	res = 0
	for numbers in numb_array:
		res += int(numbers)
	return 	res
def extract_numbers(numb_array):
	tmp_arr = []
	tmp_arr2 = []
	for item in numb_array:
		if item.find('X^1') != -1:
			tmp_arr.append(item.split('*')[0])
		else:
			tmp_arr2.append(item.split('*')[0])
	return tmp_arr, tmp_arr2

def resolve_first_degree(left, right):
	left_no_spc = left.replace(' ', '')
	right_no_spc = right.replace(' ', '')
	arr_left = left_no_spc.split('+')
	arr_right = right_no_spc.split('+')
	res_l = []
	res_r = []
	tmp_arr_left, tmp_arr_left2 = extract_numbers(arr_left)
	tmp_arr_right, tmp_arr_right2 = extract_numbers(arr_right)
	res_l.append(sum_of_num(tmp_arr_left))
	res_l.append(sum_of_num(tmp_arr_left2))
	res_r.append(sum_of_num(tmp_arr_right))
	res_r.append(sum_of_num(tmp_arr_right2))
	print (res_l, res_r)
	print (arr_left, arr_right)
	return 1

def resolve_second_degree(left, right):
	return 1

def resolve_zero_degree(left, right):
	return 1
