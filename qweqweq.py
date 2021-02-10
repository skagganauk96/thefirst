mes = "Возраст: "

while True:
	age = input(mes)
	if age == 'ex':
		break
	try:
		age = int(age)
		if age < 3:
			print("Free")
		elif age < 12:
			print("10")
		elif age > 12: 
			print("15")
	except:
			print("Cho")
