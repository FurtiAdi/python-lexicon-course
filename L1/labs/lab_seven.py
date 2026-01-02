cart_lists = []
count = 0

while count<5:
  item = input('Enter your item: ')
  cart_lists.append(item)
  count +=1


print(cart_lists)
cart_lists.pop(-1)
print(len(cart_lists))
print(cart_lists[0] + " " + cart_lists[-1])

