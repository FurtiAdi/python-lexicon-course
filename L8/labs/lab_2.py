# Task 2: Functional list transformation
ls = [1, 2, 3, 4, 5, 6, 7]

changed_list = list(map(lambda x: x ** 2, ls))
filtered_list = list(filter(lambda x : x % 2==0, changed_list))

print(changed_list)
print(filtered_list)