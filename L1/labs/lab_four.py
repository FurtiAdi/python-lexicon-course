user_input = input("Enter your name: ")

print(user_input.lower())
print(user_input.upper())
print(len(user_input))

splitted_input = user_input.split()
print(splitted_input)

#Replace first letter
user_input = 'A' + user_input[1:]
print(user_input)

