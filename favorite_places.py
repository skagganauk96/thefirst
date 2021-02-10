fav_numbers = {
	'pasha': [5, 6, 9],
	'dasha': [7],
	'kasha': [1, 2],
	'vasha': [4, 98],
	}

for name, numbers in fav_numbers.items():
	numbers = [str(number) for number in numbers]  # списочное выражение
	print(name.title() + ": " + ', '.join(numbers))
