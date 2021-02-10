minsk = {'country': 'belarus', 'population': 1.9, 'fact': 'pretty, but repressive government'}
derry = {'country': 'state man, usa', 'population': 0.3, 'fact': 'it lives here'}
dyatlovo = {'country': 'belarus', 'population': 1, 'fact': 'i am from there'}

minsk['name'] = 'minsk'
derry['name'] = 'derry'
dyatlovo['name'] = 'dyatlovo'

cities = [minsk, derry, dyatlovo]

capitalized_countries = ['gb', 'sar', 'usa', 'uk', 'rf']

for city in cities:
	country = city['country'].title()
	for cc in capitalized_countries:
		if cc in city['country']:
			country = country.replace(cc.title(), cc.upper())
			break

	
	print("\n" + city['name'].title() + " located in " + country + "." +
	" \nPopulation of it is : " + str(city['population']) + "." + 
	" Interestinf fact about "  + city['name'].title() + ": " + city['fact'] + ".")
