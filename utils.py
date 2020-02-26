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

def get_degree(numb_str):
	i = 0
	degree = -1
	while i < len(numb_str):
		if numb_str[i] == 'X' and numb_str[i + 1] == '^':
			j = i
			while j < len(numb_str) and numb_str[j] != ' ':
				j += 1
			tmp_degree = int(numb_str[i + 2: j])
			if tmp_degree > degree:
				degree = tmp_degree
		i += 1
	return degree

def count_minus(left, right):
	i = 0 
	count = 0
	while i < len(left):
		if left[i] == '-' and left[i + 4] != '0':
			print(left[i + 4])
			count += 1
		i += 1
	while i < len(right):
		if right[i] == '-' and right[i + 4] != '0':
			print(right[i + 4])
			count += 1
		i += 1	
	if count % 2 != 0:
		return 1
	else:
		return 0
	return 0