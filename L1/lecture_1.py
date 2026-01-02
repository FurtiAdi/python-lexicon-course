
#Arithmetic
print(2+2)
a=5
a = 10
a = a + a
print(a)

#Strings
str = "Hello world"
print(len(str))
print(str[0])
print(str[1:]) 
print(str[:3])
print(str[:])
print(str[-1])
print(str[:-1])
print(str[::-1])
str.upper()
str.lower()
print(str.split())
print(str.split('w'))
print(f"This is string with {str}")
print("This is string with an {p}".format(p='insert'))
print('One = {p}, Two: {p}, Three = {p}'.format(p='hi'))
print('One = {a}, Two: {b}, Three = {c}'.format(a='hi', b='hello', c='world'))

#lists
my_list = [1, 2, 3] #it is muttable, and can be accessed with index
my_list = ["one", "two", "three", 4, 5]
len(my_list)
print(my_list[0])
print(my_list[1:])
print(my_list[:3])
my_list = my_list + ['new_item']
print(my_list)
print(my_list * 2) #it will double temporary

l = [1, 2, 3]
l.append("append me")
popped_item = l.pop(0)
print(popped_item)
print(l)

new_list = ['a', 'b', 'c', 'd', 'e']
new_list.reverse()
new_list.sort() #it can't work if  items have different types
print(new_list)


lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]
print(matrix[0])
print(matrix[0][0])

first_col =[row[0] for row in matrix]
print(first_col)
