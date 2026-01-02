tup = (1,2,3,4,5,6,7,8,9,10)
new_tup = [] #create list first to append

for i in tup:
  if i%2==0:
    new_tup.append(i)
print(tuple(new_tup))