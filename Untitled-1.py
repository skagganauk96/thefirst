unconfirmed_users = ['alice', 'jason', 'freddy']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print("Verifying users: " + current_users.title())
    confirmed_users.append(current_users)

print("Проверены: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())