prompt = "\nСообщите свой возраст: "
age = " "
while True:
	age = int(input(prompt))
	
	if age < 3:
		print("Вход бесплатный")
	elif age < 12:
		print("10 баксов, плез")
	else:
		print("15 dollars, bitch!")
