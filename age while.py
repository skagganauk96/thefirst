prompt = "\nСообщите свой возраст: "

while True:
	age = input(prompt)
	if age == 'ex': break
	try:
	    age = int(age)
		if age < 3:
			print("Free")
		elif < 12:
			print("ten dollars")
		else:
			print("45 rubels")
	except:
		 print("введено не число")
