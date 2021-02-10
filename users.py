people = {
	'bruce': {'last': 'wayne', 'age': 'unknown', 'city': 'gotham'},
	'alexey': {'last': 'zhydko', 'age': 24, 'city': 'minsk'},
	'kakashi': {'last': 'unknown', 'age': 'unknown', 'city': 'animecity'},
	}
for name, full_info in people.items():
	print("\nName: " + name.title())
	print("\tDesription: last name is " + full_info['last'].title() + ". " +
		str(full_info['age']) + " years old, live in " + full_info['city'].title())
		
