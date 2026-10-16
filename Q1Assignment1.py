
username = input("Enter your username: ")

if username.isspace():
    print("Invalid: Username cannot contain only spaces")
elif len(username) < 5:
    print("Invalid: Username must have at least 5 characters")
elif username.lower() == "admin":
    print("Invalid: Username cannot be admin")
else:
    print("Valid username")
