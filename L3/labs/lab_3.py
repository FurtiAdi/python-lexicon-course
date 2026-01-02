def greeting(name='default'):
  return f'Hello, {name} Welcome!'

print(greeting('Fortuna'))
print(greeting(), end ='\n\n')

def isEven(num):
  return num%2==0

print(isEven(4))
print(isEven(5), end ='\n\n')

def addIfEven(num1, num2):
  if isEven(num1) and isEven(num2):
    return num1 + num2
  else:
    return 0
  
print(addIfEven(1,2))
print(addIfEven(2,4))