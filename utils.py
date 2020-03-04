
def sum_of_num(numb_array):
	res = 0
	for numbers in numb_array:
		res += float(numbers)
	return res
	
def extract_numbers(numb_array, degree):
	numbers = []
	unknown = []
	i = 0
	while (i < len(numb_array)):
		if numb_array[i] == '-' or numb_array[i] == '+' or (i == 0 and (numb_array[i:].find('-') > numb_array[i:].find('*') or numb_array[i:].find('-') == -1)):
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
	discriminant = (b ** 2) - (4 * a * c)
	return discriminant

def get_reduced_form(numbers, degree):
	print('Polynomial degree : '+str(degree))
	result = 'Reduced form:'
	i = degree
	j = 0
	while i >= 0:
		if numbers[j] == 0:
			pass
		elif numbers[j] > 0 and i != degree:
			result = result+' + '+str(numbers[j])+' * X^'+str(i)
		elif numbers[j] < 0:
			result = result+' - '+str(numbers[j] * -1)+' * X^'+str(i)
		else:
			result = result+' '+str(numbers[j])+' * X^'+str(i)
		i -= 1
		j += 1
	result = result +' = 0'
	print(result)


def get_results(a, b, discriminant):
	if discriminant == 0:
		if a == 0:
			print('There is no value for X that makes the equation true')
			return 1
		print('Discriminant is zero, there is one solution : ')
		print(float(-b / (2 * a)))
	elif discriminant > 0:
		print('Discriminant is strictly positive, the two solutions are: ')
		first_sol = float((-b + (discriminant ** 0.5)) / (2  * a) )
		second_sol = float((-b - (discriminant ** 0.5)) / (2  * a) )
		print(first_sol)
		print(second_sol)
	else:
		print('Discriminant is strictly negative, there is no real solution. Instead there is two imaginary solutions: ')
		first_sol_real = (-b / (2 * a))
		first_sol_im = ((- discriminant) ** 0.5) / (2* a)
		second_sol_real = first_sol_real
		second_sol_im = first_sol_im * -1
		if first_sol_im > 0:
			print(str(first_sol_real) + ' + '+str(first_sol_im)+'i')
			print(str(second_sol_real)+' - '+str(second_sol_im * -1)+'i')
		else:
			print(str(first_sol_real)+' - '+str(first_sol_im * -1)+'i')
			print(str(second_sol_real)+' + '+str(second_sol_im)+'i')


def clean_list(numb_array, part):
	new_numb_array = []
	for numbers in numb_array:
		numbers = numbers.replace(' ', '')
		numbers = float(numbers)
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
		for i in range(1, 3):
			if i not in left_x and i not in right_x:
				left_x[i] = 0
			elif i in left_x and i in right_x:
				left_x[i] += right_x[i]
			elif i in right_x:
				left_x[i] = right_x[i]	
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
			new_vars_dict[power] = float(numbers[0]) * -1
		elif power not in new_vars_dict:
			new_vars_dict[power] = float(numbers[0])
		else:
			if part == 'right':
				numbers[0] = float(numbers[0]) * -1
				new_vars_dict[power] = new_vars_dict[power] + numbers[0]
			else:
				new_vars_dict[power] = new_vars_dict[power] + float(numbers[0])
	return new_vars_dict



def get_degree(numb_str):
	i = 0
	degree = -1
	while i < len(numb_str):
		if numb_str[i] == 'X' and numb_str[i + 1] == '^':
			j = i
			while j < len(numb_str) and numb_str[j] != ' ':
				if ((numb_str[j] == '-' and numb_str[j - 1] == '^') or numb_str[j] == '.' or numb_str[j] == ','):
					return -2
				j += 1
			if numb_str[i + 2: j] >= '0' and numb_str[i + 2:j] <= '9': 
				tmp_degree = int(numb_str[i + 2: j])
			else:
				return -2
			if tmp_degree > degree:
				degree = tmp_degree
		i += 1
	return degree