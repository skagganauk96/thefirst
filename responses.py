responses = {}

polling_active = True
while polling_active:
    name = input("Introduce yourself: ")
    response = input("What kind of shit you prefer: ")

    responses[name] = response

    repeat = input("Do you wanna repaet? (yes/no) ")
    if repeat == 'no':
		    polling_active = False

print("\nRESULTS:")
for name, response in responses.items():
    print(name.title() + " prefer " + response)
