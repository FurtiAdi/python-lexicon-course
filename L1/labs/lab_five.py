first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")

username = first_name[0:3] + last_name[-3:] + birth_year[-2:]

print("Here is your username {username}".format(username=username))