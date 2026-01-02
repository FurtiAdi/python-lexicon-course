name = 'Fortuna'

def showName():
  name = 'Fortuna Eyob' #this will shadow the global variable name
  print("The Local name is: ", name)

print("The Global name is: ", name)
showName()