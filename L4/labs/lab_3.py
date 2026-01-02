text = 'I will try to stay immutable'

def globalChanger():
  global text
  text = 'Oops! I am becoming mutable'

print('Before calling globalChanger() text is: ', text)
globalChanger()
print('After calling globalChanger() text is: ', text)