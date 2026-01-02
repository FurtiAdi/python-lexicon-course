# Section 3
# 14

l1 = ['name', 'age', 'email']
l2 = ['fortuna', 27, 'furtiadi@gmail.com']

my_dict = {l1[i] : l2[i] for i in range(0, len(l1))} #assume both lists have the same length

print()
print(my_dict, end='\n\n')