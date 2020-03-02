def sum_of_num(numb_array):
	res = 0
	for numbers in numb_array:
		res += int(numbers)
	return 	res
	
def extract_numbers(numb_array, degree):
	numbers = []
	unknown = []
	i = 0
	while (i < len(numb_array)):
		if numb_array[i] == '-' or numb_array[i] == '+' or (i == 0 and numb_array[i + 1] != '-'):
			j = numb_array.find('^', i ) + 1
			if numb_array[j] == '0':
				numbers.append(numb_array[i:numb_array.find('*', i)])
			elif numb_array.find(' ', j) != -1:
				unknown.append(numb_array[i:numb_array.find(' ', j)])
			else:
				unknown.append(numb_array[i:])
		i += 1
	if degree == 0:
		return numbers
	return numbers, unknown

def get_discriminant(a, b, c):
	discriminant = (b * b)- (4 * a * c)
	return discriminant

def get_reduced_form(a, b, c, degree):
	print('Polynomial degree : '+str(degree))
	if degree == 0:
		if a == b:
			print(str(a)+'* X^0 = '+str(b)+' * X^0') 
			print('The solution is: ')
			print('All real numbers')
		else:
			print(str(a)+' is not equal to'+' '+str(b))
			print('There is no solution.')
	elif degree == 1:
		if a >= 0:
			print ('Reduced form is : '+str(b)+' * X^1 + '+str(a)+' * X^0 = 0')
		else:
			print ('Reduced form is : '+str(b)+' * X^1 - '+str(a)+' * X^0 = 0')
	else:
		pass

def get_results(a, b, discriminant):
	if discriminant == 0:
		print('Discriminant is zero, the two solutions are: ')
		get_results(a,b,discriminant)
	elif discriminant > 0:
		print('Discriminant is strictly positive, the two solutions are: ')
		get_results(a,b,discriminant)
	else:
		print('Discriminant is strictly negative, there is no real solution. Instead there is two imaginary solutions: ')
		get_results(a,b,discriminant)
def clean_list(numb_array, part):
	new_numb_array = []
	for numbers in numb_array:
		numbers = numbers.replace(' ', '')
		numbers = int(numbers)
		if part == 'right':
			numbers = numbers * -1
		new_numb_array.append(numbers)
	return new_numb_array

def get_power(vars_str):
	power_index = vars_str.find('^') + 1
	power = int(vars_str[power_index:])
	return power

def final_clean(left_x, right_x, numbers, degree):
	number = 0
	if left_x != {}:
		for x, y in zip(left_x.keys(), right_x.keys()):
			if x == y:
				left_x[x] += right_x[y]
	else:
		left_x = right_x
	for num in numbers:
		number += num
	if degree == 0:
		return number
	return left_x, number

def clean_vars(numb_array, part):
	new_vars_dict = {}
	for numbers in numb_array:
		numbers = numbers.replace(' ', '')
		numbers = numbers.split('*')
		power = get_power(numbers[1])
		if part == 'right' and power not in new_vars_dict:
			new_vars_dict[power] = int(numbers[0]) * -1
		elif power not in new_vars_dict:
			new_vars_dict[power] = int(numbers[0])
		else:
			if part == 'right':
				numbers[0] = int(numbers[0]) * -1
				new_vars_dict[power] = new_vars_dict[power] + numbers[0]
			else:
				new_vars_dict[power] = new_vars_dict[power] + int(numbers[0])
	return new_vars_dict



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
		if left[i] == '-' and left[i + left.find('^') + 1] > '0':
			left = list(left)
			left[i] = '+'
			left = "".join(left)
			count += 1
		i += 1
	i = 0
	while i < len(right):
		if right[i] == '-' and right[i + right.find('^') + 1] > '0':
			right = list(right)
			right[i] = '+'
			right = "".join(right)
			count += 1
		i += 1
	print(count)
	if count % 2 != 0:
		return 1, left, right
	else:
		return 0, left, right
	return 0, left, right