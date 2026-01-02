nums = input("Enter numbers separated by space: ")
l = [int(num) for num in list(nums.split())] #converts to list of integers
evens =  list(filter(lambda num : num%2==0, l) )

print(evens)
print(len(evens))