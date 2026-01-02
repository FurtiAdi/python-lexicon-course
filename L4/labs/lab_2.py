text = 'I am still Global'

def printer(text):
  print('The Global says ', text)
  text = 'Now, I am changing to local'
  print(text)

print(text)
printer(text)
print(text)