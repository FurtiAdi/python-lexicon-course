text = "I am global variable"

def greeting():
  text = "I am the local variable"
  print(text)

greeting()
print(text)
