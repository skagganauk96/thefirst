users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'michael',
		'last': 'curie',
		'location': 'minsk',
		},
	'alexey': {
		'first': 'alex',
		'last': 'jidko',
		'location': 'minsk',
		}
	}
	


for username, full_info in users.items():
	print("\nUsername: " + username)
	full_name = full_info['first'] + " " + full_info['last']
	location = full_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
