minsk = {'country': 'belarus', 'population': 1.9, 'fact': 'pretty, but repressive government'}
derry = {'country': 'state man, usa', 'population': 0.3, 'fact': 'it lives here'}
dyatlovo = {'country': 'belarus', 'population': 1, 'fact': 'i am from there'}

cities = [minsk, derry, dyatlovo]

for city in cities:
	print("\n" + city.title() + " located in " + city['country'] + "." +
	"Population of it is : " + str(city['population']) + "." + 
	"Interestinf fact about "  + ": " + city['fact'] + ".")
