username = 'rabby'
get_username = input("Enter username >").lower()
if get_username == username:
    print(f"Welcome: {get_username}.")
elif len(get_username) > len(username):
    print(f"Fucker you tried to inject me!!")
else:
    print("Not valid")        