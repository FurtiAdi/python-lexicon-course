l = [1,2,3,4,5,6,]
#prints a list of squares using a loop 
result = []
for i in l:
  result.append(i**2)
print(result)

#prints a list of squares using a list comprehension 
result = [i**2 for i in l]
print(result)

#prints a list of positive numbers using a comprehension 
l = [-1,-2,-3,-4,1,2,3,4,5,6]
result = [i for i in l if i > 0]
print(result)