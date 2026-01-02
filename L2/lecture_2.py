
# String Reminder
print("Me name is {name} and I'm {age} year's old".format(name='Fortuna', age=27))
name = 'Fortuna'
age = 27
print(f"My name is {name} and I'm {age} years old")

# Mapping
my_dictionary = {
  1:'value1',
  2:'value2',
  3:'value3',
  'three' : 3,
  4: ['name1', 'name2', 'name3'],
  4 : 'value ?' #it will replace the first key value
}

print(my_dictionary[1])
print(my_dictionary[2])
print(my_dictionary['three'])
print(my_dictionary[4])

print(my_dictionary[4][0])
print(my_dictionary[4][0].upper())

my_dictionary[1] = 'updated value1'
print(my_dictionary)

my_dictionary[4] += ['name4']
print(my_dictionary[4])

#Add to dictionary
new_dictionary = {}

new_dictionary['student'] = 'Fortuna'
new_dictionary['age'] = 27
new_dictionary['school'] = 'Lexicon'
print(new_dictionary)

#Nested dictionary
nested_dictionary = {
  'person1' : {
    'name' : {
      'first': 'Fortuna',
      'last' : 'Eyob'
    },
    'age' : 27
  },
  'person2' : {
    'name' : 'Robel',
    'age' : 26
  },
  'person3' : {
    'name' : 'Maku',
    'age' : 26
  }
}

print(nested_dictionary)
print(nested_dictionary['person1']['name']['first'])

#Methods
dictionary = {
  'key1' : 1,
  'key2' : 2,
  'key3' : 3
}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

#Tuple
my_tuple = (1,2,3,'four') #index can be used, immutable, used where immutability is usefull
print(len(my_tuple))
print(my_tuple[0])
print(my_tuple.index('four'))
print(my_tuple.count(1))

#my_tuple[0] = 5 ##immutable
print(my_tuple)

#Sets
#Mutable
x = set()
x.add(1)
print(x)

my_set={1,2,3}
my_set.add(4)
my_set.add(3) #No dublicate
print(my_set)

my_lists = [1,2,3,4,5,6,1,2,3,4,5,6]
print(set(my_lists))

#Boolean
a = True
b = False

print(1>2)
print(a>b)

#Control flow
print(1 == 1)
print(1 == '1') #can't compare integer with string
print('hi' == 'bye')
print('1' == '1')
print(1 != 2)

print((1<2) and (2>3))
print((1<2) or (2>3))

#in python we dont use semi colon at the end of each statement like in Java ;
#but indentation is used

#if-else-statement
if 1 < 2:
  print("Yes")
elif 1 == 2:
  print('Yay!')
else:
  print('No')

  # Loops #
# for-loop
sequence = [1,2,3,4,5]

for item in sequence:
  print(item) 

for i in range(0,5):
  print(sequence[i], end=' ')
  
ages = {
  'fortuna' : 27,
  'robel' : 26
}

for key in ages:
  print("This is the age: ")
  print(key)
  print("This is the value: ")
  print(ages[key])
  print('\n')

my_pairs = [(1,10), (2,20), (3,30)] #Tuple unpacking

for tup in my_pairs:
  print(tup)

for item1, item2 in my_pairs: 
  print(item1)
  print(item2)

# no_pairs = [1,2,3] #Nothing to unpack

# for item1, item2 in no_pairs:
#   print(item1)
#   print(item2)

# While-loop
i=1
while i < 5:
  print('i is: {}'.format(i))
  i += 1
print("End")


