user_input = input("Enter numbers separated by space: ")
print(user_input) #to check how output looks

l = [int(x) for x in user_input.split()]

new_list = [x for x in l if x%2==0]

print(new_list)