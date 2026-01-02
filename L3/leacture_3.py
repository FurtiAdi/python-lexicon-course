#Range
# Range always starts on 0 goes upto n
for i in range (5, 10):
  print(i)

for i in range (2, 10, 2):
  print(i)

nums = list(range(5))
print(nums)

x = [1,2,3]
out = []

for item in x:
  out.append(item**2)
print(out)

print([item**2 for item in x])

# Function
# Groups together a set of statement
# Reusabilty of code

def my_func(parameter = 'default'):
  print(parameter)

def hello():
  print('hello')

hello()

def giveMeHello():
  return "Hello!"

result = giveMeHello()
print(result)

def evenCheck(num):
  print("I am checking to see if {} is even".format(num))
  print(num%2==0)

evenCheck(41)

def helloYou(name="Default"):
  return ("Hello, " + name)

result = helloYou('Fortuna')
print(result)

def addEvenOnly(num1, num2):
  if num1 % 2 != 0 or num2%2!=0:
    return False
  else:
    return num1 + num2

y = addEvenOnly(1,2)
x = addEvenOnly(2,2)

print(y)
print(x)

def timesTwo(num):
  return num * 2

lambda num: num * 2 #Use it if the function will be used only once

my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
  return num%2==0

evens = filter(evenBool, my_list)
print(list(evens))

evens = filter(lambda num: num%2==0, my_list)
print(list(evens))


#Methods of Strings
st = "hello my name is Fortuna"
st.lower()
st.upper()
st.split()

#Methods of dictionaries
d = {'k1' : 1, 'k2' : 2}
d.keys()
print(d.items())

#Methods and functions are different???CHECK

# def func(a, b, c=10, d=11):
#   print(a, b, c)

def func(*args):
  print(args)

func()
func(1)
func(1,2,3)

def func2(a,b, **kwargs): #**kwargs is dict
  print(a, b)
  print(kwargs)

func2(1,2,c=12,d=17)

def func3(a, b, *args, name='fortuna', **kwargs):
  print('a={}'.format(a))
  print('b={}'.format(b))
  print('args = {}'.format(args))
  print('name = {}'.format(name))
  print('kwargs = {}'.format(kwargs))

func3(1, 2)
func3(1, 2, 3, name = 'Anna', age = 35, email = 'ann@email.com')

